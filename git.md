
## short and sweet example. Here I am creating a tag named v1.1 of my code and pushing it to origin

# Once you are satisfied with your code
````
git tag -a v1.1 -m "this is a message to remember what this tag is about"
````

# To view your current tags
````
git tag
````
# To push your tag to origin
````
git push origin v1.1
````

If at some point you need to checkout the tag
# This will checkout the tag as a branch
````
git checkout -b <branch name> v1.1
````

 