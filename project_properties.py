DB_CONFIG = {
    '4gnews': {
        'DB_USER': '4gnews',
        'DB_NAME': '4gnews',
        'DB_HOST': '127.0.0.1',
        'SQL_PORT': 3306,
        'SSH_PORT': 22,
        'SSH_HOST': 'fr.d.7gra.us',
        'SSH_USER': 'ubuntu'},
    'blipzi': {
        'SSH_HOST': 'ca.b.7gra.us',
        'SSH_USER': 'ubuntu',
        'SSH_PORT': 22,
        'DB_HOST': '127.0.0.1',
        'DB_PORT': 3306,
        'DB_USER': 'blipzi',
        'DB_PASS': 'Rh*t7t969vCF#v9JuzVR',
        'DB_NAME': 'blipzi_v1',
        'SQL_PORT': 3306}
}

BQ_CONFIG = {
    'SERVICE_ACCOUNT_FILE': '/Users/nunoseica/Downloads/ad_manager_key.json',
    'PROJECT': 'analytics-341715',
    'PROD_DATASET': 'Group_Content_Creators',
    'PROD_TABLE': 'Content_Production',
    'WRITE_DISPOSITION': ['WRITE_TRUNCATE', 'WRITE_APPEND']
}
