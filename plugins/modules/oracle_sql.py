#!/usr/bin/python
DOCUMENTATION = '''
---
module: jmsierra.oracle.oracle_sql
short_description: Execute arbitrary sql
description:
    - Execute arbitrary sql against an Oracle database
version_added: "0.2.0
options:
    username:
        description:
            - The database username to connect to the database
        required: false
        default: None
        aliases: ['user']
    password:
        description:
            - The password to connect to the database
        required: false
        default: None
        aliases: ['pass']
    mode:
		description:
			- The mode with which to connect to the database
		required: false
		default: normal
		choices: ['normal','sysdba', 'sysasm']
    hostname:
        description:
            - The host of the database
        required: false
        default: localhost
        aliases: ['host']
    port:
        description:
            - The listener port to connect to the database
        required: false
        default: 1521
    service_name:
        description:
            - The service_name to connect to the database
        required: false
        default: database_name
        aliases: ['sn']
    connection_string:
        description:
            - The connection string used to connect to the database
        required: false
    sql:
        description:
            - The sql you want to execute
        required: false
    script:
        description:
            - The script you want to execute. Doesn't handle selects
        required: false
notes:
    - cx_Oracle needs to be installed
    - Oracle client libraries need to be installed along with ORACLE_HOME and LD_LIBRARY_PATH settings.
requirements: [ "cx_Oracle" ]
author: Mikael Sandström, oravirt@gmail.com, @oravirt
'''

from logging import exception
from sqlite3 import DatabaseError
from ansible.module_utils.basic import AnsibleModule
import cx_Oracle
from ansible_collections.jmsierra.oracle.plugins.module_utils.oracle_utils import connect,execute_sql

def run_module():
    # Define Module arguments
    module = AnsibleModule(
        argument_spec=dict(
            username=dict(required=False, aliases=['user']),
            password=dict(required=False, no_log=True, aliases=['pass']),
            mode=dict(default="normal", choices=["sysasm", "sysdba", "normal"]),
            service_name=dict(required=False, aliases=['sn']),
            hostname=dict(required=False, default='localhost', aliases=['host']),
            port=dict(required=False, default=1521),
            connection_string=dict(required=False),
            sql=dict(required=True)
        ),
        mutually_exclusive=[['sql', 'script'],
                            ['connection_string', 'hostname'], 
                            ['connection_String', 'port'], 
                            ['connection_string', 'service_name']]
    )

    try:
        # Create database connection
        connection = connect(username=module.params['username'],
                            password=module.params['password'],
                            mode=module.params['mode'],
                            hostname=module.params['hostname'],
                            port=module.params['port'],
                            service=module.params['service_name'],
                            connection_string=module.params['connection_string'])
    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        msg = 'Could not connect to database: %s'.format(error.message)
        module.fail_json(msg=msg, changed=False)
        
    try:
        # Execute query
        with connection.cursor() as cursor:
            result = execute_sql(connection, cursor, module.params["sql"])

        connection.commit()

        module.exit_json(changed=(result.get('rows_affected') > 0), 
                        data=result.get('data'), 
                        rows_affected=result.get('rows_affected'))


    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        msg = 'Failed to execute statement: %s'.format(error.message)
        module.fail_json(msg=msg, changed=False)

    finally:
        connection.close()


def main():
    run_module()

if __name__ == '__main__':
    main()
