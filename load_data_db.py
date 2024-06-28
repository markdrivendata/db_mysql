import pandas as pd
from project_properties import BQ_CONFIG
from google.cloud import bigquery


class LoadDataDb:

    def __init__(self, key_path: str):
        self.key_path = key_path
        self._initialize_bigquery()

    def _initialize_bigquery(self):
        self.bq_client = bigquery.Client.from_service_account_json(self.key_path)

    def load_data_bq(self, data_frame: pd.DataFrame):

        if data_frame is not None and not data_frame.empty:

            # GCP - Big Query config
            PROJECT = BQ_CONFIG['PROJECT']
            PROD_DATASET = BQ_CONFIG['PROD_DATASET']
            PROD_TABLE = BQ_CONFIG['PROD_TABLE']

            # Create a load job config
            job_config = bigquery.LoadJobConfig()
            self.bq_client.load_table_from_dataframe(data_frame, '.'.join([PROJECT, PROD_DATASET, PROD_TABLE]),
                                                     job_config=job_config)

        else:
            return print('No data to load')

        return print(f'Data loaded in prod dataset -> {PROD_TABLE}')
