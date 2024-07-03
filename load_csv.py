import pandas as pd
from google.cloud import bigquery
from project_properties import BQ_CONFIG

data = pd.read_csv('/Users/nunoseica/Downloads/query_result.csv', names=['year', 'month', 'content_totals',
                                                                         'product', 'content_type', 'content_freshness'])
print(data)


def main(df):

    # GCP - Big Query config
    PROJECT = 'analytics-341715'
    DATASET = 'Group_Content_Creators'
    TABLE = 'Content_Production'

    # Establish a BigQuery client
    client_bq = bigquery.Client.from_service_account_json(BQ_CONFIG['SERVICE_ACCOUNT_FILE'])
    project_id = PROJECT
    dataset_id = DATASET
    table_name = TABLE

    # Create a job config
    job_config = bigquery.LoadJobConfig()

    # Set the destination table
    load_job = client_bq.load_table_from_dataframe(df, '.'.join([PROJECT, DATASET, TABLE]), job_config=job_config)
    return 'Data Loaded'


data = pd.read_csv('/Users/nunoseica/Downloads/query_result.csv', names=['year', 'month', 'content_totals',
                                                                         'product', 'content_type', 'content_freshness'])
print(data)
main(data)
