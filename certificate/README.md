### Oh what headaches this error can cause you when you are just trying to get some work done.

> requests.exceptions.SSLError: (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1131)')))

This can happen even if your app works just fine with HTTPs when you access it through a browser. I tried many things, which did not work. This worked for me. Hope this post will help some other people as well.

````
So my app looked like this
import ssl
context = ssl.SSLContext()
context.load_cert_chain('/path/to/certificate.crt', '/path/to/certificate.key')
app.run(host="0.0.0.0", port=portnumber, ssl_context=context)
````

Now the problem I had was that I actually had two certificate files, a .crt and a .ca-bundle:

>    The .crt was my server certificate (issued specifically for my domain)
     The ca-bundle is a file that contains root and intermediate certificates

The certificate chain is composed of both the server AND the CA bundle certificates, so if you did not receive them pre-combined, for Flask to run well you should combine them into a single file and use that file as the first argument of your ssl context tuple. For more info on how this security chain of trust works, see some of the links at the end of the article.

See image credit: 640px-Chain_of_trust_v2.svg_.png

Long story short, you really need both in the same file. So here is a very simple way you can do this with the command line:

> ### First, just copy the contents of .crt
> cat your_server_speficic_certificate.crt > chain_certificate.crt
> ### Then simply append the contents of the .ca-bundle
> cat your_root_and_intermediate.ca-bundle >> chain_certificate.crt

````
If you’ve received any other 3rd party intermediate certificates, you can add them in the same way. In the end your new file should look like this
-----BEGIN CERTIFICATE-----
(your domain .crt contents)
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
(Contents of your .ca-bundle)
-----END CERTIFICATE----
````

### Now you can simply update your python code to refer to the updated file instead
```
import ssl
context = ssl.SSLContext()
context.load_cert_chain(
'/path/to/chain_certificate.crt',
'/path/to/certificate.key'
)
app.run(host="0.0.0.0", port=portnumber, ssl_context=context)

```
That fixed the problem for me. Hope it helps you as well.


Further Reading:

    https://en.wikipedia.org/wiki/Chain_of_trust
    https://www.ssldragon.com/blog/certificate-authority
    https://venafi.com/blog/what-difference-between-root-certificates-and-intermediate-certificates
