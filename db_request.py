import pymysql
from sshtunnel import SSHTunnelForwarder
import pandas as pd


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



