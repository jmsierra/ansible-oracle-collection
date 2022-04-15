import cx_Oracle
import re

def connect(username, password, mode='normal', hostname = None, port = 1521, service = None, connection_string = None):
    ''' Establish a database connection as per parameters provided
    '''
    dsn = None
    conn = None

    # If connection string is passed, use that one as dsn;
    # if not, build it from hostname, port and service
    if connection_string:
        dsn = connection_string
    else:
        dsn = cx_Oracle.makedsn(host=hostname, port=port, service_name=service)

    # Establish the connection
    if mode == 'sysdba':
        conn = cx_Oracle.connect(username, password, dsn, mode=cx_Oracle.SYSDBA)
    elif mode == 'sysasm':
        conn = cx_Oracle.connect(username, password, dsn, mode=cx_Oracle.SYSASM)
    else:
        conn = cx_Oracle.connect(username, password, dsn)

    # Return the connection
    return conn


def execute_sql(conn, cursor, sql):
    ''' Execute a SQL query and return its results
    '''
    sql = sql.strip()
        
    if re.match('^select', sql, re.I):
        sql = sql.rstrip(';')
        cursor.execute(sql)
        
        descriptors = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        
        return {'data': [dict(zip(descriptors, r)) for r in rows], 'rows_affected': len(rows)}
    
    elif re.match('^update', sql, re.I) or re.match('^delete', sql, re.I) or re.match('^insert', sql, re.I):
        sql = sql.rstrip(';')
        cursor.execute(sql)
        return {'data': [], 'rows_affected': cursor.rowcount}
    
    else:
        # begin or declare
        cursor.callproc("dbms_output.enable")
        chunk_size = 1000

        # create variables to hold the output
        lines_var = cursor.arrayvar(str, chunk_size)
        num_lines_var = cursor.var(int)
        num_lines_var.setvalue(0, chunk_size)

        # fetch the text that was added by PL/SQL
        while True:
            cursor.callproc("dbms_output.get_lines", (lines_var, num_lines_var))
            num_lines = num_lines_var.getvalue()
            lines = lines_var.getvalue()[:num_lines]
            for line in lines:
                print(line or "")
            if num_lines < chunk_size:
                break
        
        return {'data': lines, 'rows_affected': 0}
