# ansible-oracle-collection

## Important notes
This ansible collection and its roles tries to ease Oracle database-related product installations and management. Please make sure you have the rights and/or required licenses to use Oracle products before using it.  

Included and adapted modules from https://github.com/oravirt/ansible-oracle-modules. 

## Requirements
None

## Roles
| Role | Build Status | Documentation |
| ---- | ------------ | ------------- | 
| jmsierra.oracle.instantclient | [![jmsierra.oracle.instantclient](https://github.com/jmsierra/ansible-oracle-collection/actions/workflows/instantclient.yml/badge.svg)](https://github.com/jmsierra/ansible-oracle-collection/actions/workflows/instantclient.yml) | [Documentation](https://github.com/jmsierra/ansible-oracle-collection/blob/main/roles/instantclient/README.md) |

## Modules
| Module | Description |
| ------ | ----------- |
| jmsierra.oracle.grants | Manages Oracle privileges through grants |
| jmsierra.oracle.role | Manages Oracle Roles |
| jmsierra.oracle.sql | Executes SQL queries against database |
| jmsierra.oracle.user | Manages Oracle Schemas |
