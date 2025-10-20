Step 1: List current sessions on your database server
# Postgres query
````
select pid, usename, datname, state, backend_start, query_start, client_addr, client_hostname from pg_stat_activity;
````

Where:
    pid: Process ID of this backend
    usename: Name of the user logged into this backend
    datname: Name of the database this backend is connected to
    state: Current overall state of this backend:
        active: The backend is executing a query
        idle: The backend is waiting for a new client command
    backend_start: Time when this process was started. For client backends, this is the time the client connected to the server.
    query_start: Time when the currently active query was started, or if state is not active, when the last query was started
    client_addr: IP address of the client connected to this backend. If this field is null, it indicates either that the client is connected via a Unix socket on the server machine or that this is an internal process such as autovacuum.
    client_hostname: Host name of the connected client, as reported by a reverse DNS lookup of client_addr

For a complete description of all available fields you can check the documentation.
Step 2: Delete sessions/connections

Once you have identified which process ID (pid) you want to kill, just do the following:

# Replace PID with your actual process ID
````
select pg_cancel_backend(PID); select pg_terminate_backend(PID);
````
That should be it.