DB_HOST = "localhost"
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"

#!/usr/bin/python

from subprocess import PIPE,Popen

def dump_table(host_name,database_name,user_name,database_password,table_name):

    command = 'pg_dump -h {0} -d {1} -U {2} -p 5432 -t {3} -Fc -f /Users/syed/Documents/{3}_B.psql'\
    .format(host_name,database_name,user_name,table_name)

    p = Popen(command,shell=True,stdin=PIPE)

    return 1 #p.communicate('{}\n'.format(database_password))


def main():
    dump_table('localhost','postgres','postgres','postgres','users')
    dump_table('localhost','postgres','postgres','postgres','bird')
    dump_table('localhost','postgres','postgres','postgres','card_asset')
    dump_table('localhost','postgres','postgres','postgres','game')
    dump_table('localhost','postgres','postgres','postgres','habitat')
    dump_table('localhost','postgres','postgres','postgres','food')
 
if __name__ == "__main__":
    main()