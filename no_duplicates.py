from google.cloud import bigquery
from project_properties import BQ_CONFIG


def overwrite_data(key_path: str):
    # Establish a BigQuery client
    client_bigquery = bigquery.Client.from_service_account_json(key_path)

    # Overwrite data
    sql_query_ddl = f"""
    DELETE
    FROM
    `{BQ_CONFIG['PROJECT']}.{BQ_CONFIG['PROD_DATASET']}.{BQ_CONFIG['PROD_TABLE']}`
        WHERE
            product IS NOT NULL
        """

    # Run the query to overwrite data
    overwrite = client_bigquery.query(sql_query_ddl)
    overwrite.result()
    return print(f"Ready to load data in -> {BQ_CONFIG['PROD_TABLE']}")
