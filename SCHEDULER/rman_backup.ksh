## This script take backup of database using RMAN ( recovery manager tool) of ORACLE.
##location of file is - /appl/bin/rman_backup.ksh
#!/bin/bash

##Assume path of RMAN $ORACLE_HOME/bin
export RMAN_HOME=$ORACLE_HOME/bin/

##Connect Target( Assumming user have admin access)
rman connect target <<EOF

##Back (dbf file would be created)
backup as backupset database
EOF