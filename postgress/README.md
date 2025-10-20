# This can work locally as well, just replace any local host names by localhost
> #### Dump the table from the source database
> PGPASSWORD="source-db-password" pg_dump -h source-db-hostname -U source-db-username -d source-database-name -t source-table-to-copy > table-to-copy.sql
> #### Now you can load the table into the destination database
> PGPASSWORD="destination-db-password" psql -h destination-db-hostname -U destination-db-username -d destination-database-name -f table-to-copy.sql



#### To copy multiple tables at the same time, do
> #### Dump tables 1, 3 and 3 from the source database
> PGPASSWORD="source-db-password" pg_dump -h source-db-hostname -U source-db-username -d source-database-name -t table1 -t table2 -t table3 > table-to-copy.sql



#### To copy the table structure only (without the data), do
> ### # Dump tables 1 and 2, but just their structure (schema)
> PGPASSWORD="source-db-password" pg_dump -h source-db-hostname -U source-db-username -d source-database-name -t table1 -t table2 --schema-only > table-to-copy.sql
command line copy



### Because every time you want to do it, you realize that you forgot how you did it the last time.

## Only export the schema of a database

#### This will explort the schema of all of the tables with your database
> ####  If your database is on the server/computer you are currently in, you can drop the -h hostname/IP
> PGPASSWORD="your-db-password" pg_dump -h <hostname/IP> -U <username> -d <name-of-database> --schema-only > database_schema.sql


#### Only export the schema of a particular table
> ####  This will only copy the schema of table_name
> PGPASSWORD="your-password" pg_dump -h <hostname/IP> -U <username> -d <name-of-database> -t <table_name> --schema-only > table-schema.sql

#### Example with multiple tables
> ####  This will only copy the schema of table1 and table2
> PGPASSWORD="your-password" pg_dump -h <hostname/IP> -U <username> -d <name-of-database> -t <table1> -t <table2> --schema-only > tables-1-2-schema.sql

# ref
https://github.com/NaysanSaran/pandas2postgresql/tree/master
 
