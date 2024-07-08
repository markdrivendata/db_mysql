import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder
import pandas as pd
from os.path import expanduser

SSH_HOST = 'fr.d.7gra.us'
SSH_USER = 'ubuntu'
SSH_PORT = 22
DB_HOST = 'localhost'
SQL_PORT = 3306
DB_USER = '4gnews'
DB_PASS = 'TJ4Dhw9p6GGysUk5'
DB_NAME = '4gnews'
path = '/.ssh/id_rsa'

home_dir = expanduser('~')

key_ssh = paramiko.RSAKey.from_private_key_file(home_dir + path)


def db_data(key):
    with SSHTunnelForwarder((SSH_HOST, SSH_PORT),
                            ssh_username=SSH_USER,
                            ssh_pkey=key,
                            remote_bind_address=(DB_HOST, SQL_PORT)) as tunnel:
        client = pymysql.connect(user=DB_USER,
                                 password=DB_PASS,
                                 host=DB_HOST,
                                 port=tunnel.local_bind_port,
                                 database=DB_NAME,
                                 connect_timeout=60,
                                 read_timeout=60)
        cursor = client.cursor()
        cursor.execute("""
       SELECT
      *
        FROM
            articles
  LIMIT
  5

                """)
        rows = cursor.fetchall()
        header = [i[0] for i in cursor.description]

        df = pd.DataFrame(rows, columns=header)

        cursor.close()
        client.close()

    return print(df)


db_data(key_ssh)
