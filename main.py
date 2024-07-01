from project_properties import DB_CONFIG, BQ_CONFIG
from db_request import MySqlDataRequest
from sql_query import QUERIES
import paramiko
from os.path import expanduser
from no_duplicates import overwrite_data
from load_data_db import LoadDataDb


def print_hi(name):
    # Build key
    path = '/.ssh/id_rsa'
    home_dir = expanduser('~')
    key_ssh = paramiko.RSAKey.from_private_key_file(home_dir + path)

    # Build clients
    client_mysql = MySqlDataRequest(key=key_ssh)
    client_bq = LoadDataDb(key_path=BQ_CONFIG['SERVICE_ACCOUNT_FILE'])

    # No duplicates in Prod Currency Dataset
    overwrite_data(key_path=BQ_CONFIG['SERVICE_ACCOUNT_FILE'])

    # Request by project
    for i in DB_CONFIG:
        for j in QUERIES:
            if i == j:
                df = client_mysql.data_request(ssh_host=DB_CONFIG[i]['SSH_HOST'], ssh_port=DB_CONFIG[i]['SSH_PORT'],
                                               ssh_user=DB_CONFIG[i]['SSH_USER'], db_user=DB_CONFIG[i]['DB_USER'],
                                               db_host=DB_CONFIG[i]['DB_HOST'], db_pass=DB_CONFIG[i]['DB_PASS'],
                                               db_name=DB_CONFIG[i]['DB_NAME'], sql_port=DB_CONFIG[i]['DB_PORT'],
                                               query=QUERIES[j])
                # Load data in Prod
                client_bq.load_data_bq(data_frame=df)
                print(f"Data of project {i} -> loaded in prod!")

    print(f'Data loaded -> {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Content_Production')
