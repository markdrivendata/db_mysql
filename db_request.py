import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder
import pandas as pd
from os.path import expanduser
from sql_query import query_blipzi_com
from project_properties import DB_CONFIG

path = '/.ssh/id_rsa'
home_dir = expanduser('~')
key_ssh = paramiko.RSAKey.from_private_key_file(home_dir + path)


class MySqlDataRequest:

    def __init__(self, key):
        self.key = key

    def data_request(self, ssh_host: str, ssh_port: str,
                     ssh_user: str, db_user: str,
                     db_host: str, db_pass: str,
                     db_name: str, sql_port: str,
                     query: str):
        with SSHTunnelForwarder((ssh_host, ssh_port),
                                ssh_username=ssh_user,
                                ssh_pkey=self.key,
                                remote_bind_address=(db_host, sql_port)) as tunnel:
            client = pymysql.connect(user=db_user,
                                     password=db_pass,
                                     host=db_host,
                                     port=tunnel.local_bind_port,
                                     database=db_name,
                                     connect_timeout=60,
                                     read_timeout=60)
            cursor = client.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            header = [i[0] for i in cursor.description]

            df = pd.DataFrame(rows, columns=header)

            cursor.close()
            client.close()

        return print(df)


client_mysql = MySqlDataRequest(key=key_ssh)
client_mysql.data_request(ssh_host=DB_CONFIG['blipzi']['SSH_HOST'], ssh_port=DB_CONFIG['blipzi']['SSH_PORT'],
                          ssh_user=DB_CONFIG['blipzi']['SSH_USER'], db_user=DB_CONFIG['blipzi']['DB_USER'],
                          db_host=DB_CONFIG['blipzi']['DB_HOST'], db_pass=DB_CONFIG['blipzi']['DB_PASS'],
                          db_name=DB_CONFIG['blipzi']['DB_NAME'], sql_port=DB_CONFIG['blipzi']['SQL_PORT'],
                          query=query_blipzi_com)
