import pandas as pd
from google.cloud import bigquery

file_path = '/Users/nunoseica/Downloads/query_result.csv'


class LoadDataManually:

    def __init__(self, csv_path):
        self.csv_path = csv_path

    def read_csv(self):
        df = pd.read_csv(self.csv_path)
        df = df.rename(columns={'number_articles': 'content_totals'})
        return df

    def load_bq(self):

        dataframe = self.read_csv()
        # GCP - Big Query config
        PROJECT = 'analytics-341715'
        DATASET = 'Group_Content_Creators'
        TABLE = 'Content_Production'

        SERVICE_ACCOUNT_FILE = '/Users/nunoseica/Downloads/google-analytics-api.json'

        # Establish a BigQuery client
        client_bq = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)
        project_id = PROJECT
        dataset_id = DATASET
        table_name = TABLE

        # Create a job config
        job_config = bigquery.LoadJobConfig()

        # Set the destination table
        load_job = client_bq.load_table_from_dataframe(dataframe, '.'.join([PROJECT, DATASET, TABLE]),
                                                       job_config=job_config)
        load_job.result()
        return print(f'Data Loaded in the Production Table: {TABLE}')

load_data = LoadDataManually(file_path)
load_data.load_bq()
