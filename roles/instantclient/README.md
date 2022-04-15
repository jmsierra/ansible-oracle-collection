# jmsierra.oracle.instantclient
## Description
It install Oracle Instant Client from zip files from: https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html

## Variables
| Variable | Mandatory | Default | Comment |
| -------- | --------- | ------- | ------- |
| oracle_instantclient_version | NO | `21.4` | Oracle Instant Client version to be installed. |
| oracle_instantclient_basic_url | NO | `https://download.oracle.com/otn_software/linux/instantclient/{{ oracle_instantclient_version \| regex_replace('\\.', '') }}000/instantclient-basic-linux.x64-{{ oracle_instantclient_version }}.0.0.0dbru.zip` | URL where to download instantclient basic package from |
| oracle_instantclient_sqlplus_url | NO | `https://download.oracle.com/otn_software/linux/instantclient/{{ oracle_instantclient_version \| regex_replace('\\.', '') }}000/instantclient-sqlplus-linux.x64-{{ oracle_instantclient_version }}.0.0.0dbru.zip` | URL where to download instantclient sqlplus package from |
