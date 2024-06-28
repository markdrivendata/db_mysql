import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder
import pandas as pd
from os.path import expanduser

SSH_HOST = 'ca.b.7gra.us'
SSH_USER = 'ubuntu'
SSH_PORT = 22
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'blipzi'
DB_PASS = 'Rh*t7t969vCF#v9JuzVR'
DB_NAME = 'blipzi_v1'
SQL_PORT = 3306
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
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(game_id) AS number_articles,
            'blipzi.com' AS product,
            'Game' AS content_type,
            'New content' AS content_freshness
        FROM
            games
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, game_id, NULL)) AS number_articles,
            'blipzi.com' AS product,
            'Game' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            games
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_created) AS year,
            MONTH(date_created) AS month,
            COUNT(id) AS number_articles,
            'blipzi.com' AS product,
            'Categories' AS content_type,
            "" AS content_freshness
        FROM
            categories
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_created),
            MONTH(date_created)
                """)
        rows = cursor.fetchall()
        header = [i[0] for i in cursor.description]

        df = pd.DataFrame(rows, columns=header)

        cursor.close()
        client.close()

    return print(df)


db_data(key_ssh)


