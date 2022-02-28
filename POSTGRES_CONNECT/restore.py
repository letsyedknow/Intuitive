DB_HOST = "localhost"
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"

#!/usr/bin/python

from subprocess import PIPE,Popen
from datetime import date

def restore_table(host_name,database_name,user_name,database_password,table_name):

    command = 'pg_restore -h {0} -d {1} -U {2} -p 5432 -t public.{3}< /Users/syed/Documents/{3}_B.psql'\
    .format(host_name,database_name,user_name,table_name)



    p = Popen(command,shell=True,stdin=PIPE)

    return 1 #p.communicate('{}\n'.format(database_password))

def main():
    
    restore_table('localhost','postgres','postgres','postgres','users')

if __name__ == "__main__":
    main()