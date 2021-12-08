# ansible-oracle-collection

## Important note
This ansible collection and its roles tries to ease Oracle database-related product installations and management. Please make sure you have the rights and/or required licenses to use Oracle products before using it.  

## Requirements
None

## Role jmsierra.oracle.instantclient
It install Oracle Instant Client from zip files from: https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html

Variable | Mandatory | Default | Comment
-------- | --------- | ------- | -------
oracle_instantclient_version | NO | 21.4 | Oracle Instant Client version to be installed.
