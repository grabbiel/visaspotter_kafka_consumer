import os
# DB CREDENTIALS
DB_USER = os.environ.get('AWS_RDS_VISASPOTTER_USER')
DB_PASSWORD = os.environ.get('AWS_RDS_VISASPOTTER_PASSWORD')
DB_HOSTNAME = os.environ.get('AWS_RDS_VISASPOTTER_HOSTNAME')
DB_DBNAME = os.environ.get('AWS_RDS_VISASPOTTER_DBNAME')