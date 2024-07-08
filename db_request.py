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
                     query: str) -> pd.DataFrame:
        with SSHTunnelForwarder((ssh_host, ssh_port),
                                ssh_username=ssh_user,
                                ssh_pkey=self.key,
                                remote_bind_address=(db_host, sql_port)) as tunnel:
            client = pymysql.connect(user=db_user,
                                     password=db_pass,
                                     host=db_host,
                                     port=tunnel.local_bind_port,
                                     database=db_name,
                                     connect_timeout=90,
                                     read_timeout=90)
            cursor = client.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            header = [i[0] for i in cursor.description]

            dataframe = pd.DataFrame(rows, columns=header)
            # Data transformations
            df = dataframe.rename(columns={'number_articles': 'content_totals'})
            df.fillna(0)
            df['year'] = df['year'].astype('str')
            df['year'] = df['year'].replace('nan', '0')
            df['year'] = pd.to_numeric(df['year'])
            df['year'] = df['year'].astype('int')
            df['month'] = df['month'].astype('str')
            df['month'] = df['month'].str.replace('nan', '1')
            df['month'] = pd.to_numeric(df['month'])
            df['month'] = df['month'].astype('int')

            cursor.close()
            client.close()

        return df



