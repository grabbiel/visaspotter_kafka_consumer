import pymysql, sys, os
from typing import Union

from utils.aws_credentials import get_dynamodb_client

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.db import DB_DBNAME
from config.db import DB_HOSTNAME
from config.db import DB_PASSWORD
from config.db import DB_USER



# connec to RDS db
def set_db_connection(host: str, port: int, user: str, password: str, database: str) -> Union[pymysql.connections.Connection, None]:
    conn = None
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            database=database
        )
        return conn
    except pymysql.connect.Error as E:
        print(E)
    return conn

def get_cursor(conn: pymysql.connections.Connection) -> pymysql.cursors.Cursor:
    cursor = conn.cursor()
    return cursor

def query_match_review_new_entry(cursor: pymysql.cursors.Cursor, legal_name: str, platform_code: int, alternate_name: str, code: int, country_code: int) -> None:
    cursor.execute(f"""
    INSERT INTO match_review (uscis, job_board, alternate_name, uscis_id, country, confirmation, reviewed) 
    VALUES ('{legal_name}', {platform_code}, '{alternate_name}', {code}, {country_code}, {0}, {0});
    """)
    return None

def match_review_process(cursor, match_review):
    print(match_review)
    query_match_review_new_entry(cursor, match_review["originalName"], int(match_review["platform"]), match_review["matchName"], int(match_review["code"]), int(match_review["country"]))
    return None



# connect to DynamoDB
def get_dynamodb_table_manager():
    dynamodb_client = get_dynamodb_client()

    table_manager = dynamodb_client.Table("h1b-visadata-dynamodb")
    return table_manager

def put_dynamodb_table_item(table_manager, item):
    try:
        response = table_manager.put_item(
            Item={"matchTrainId": 10, "item": item}
        )
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        print(status_code)
        return status_code
    except Exception as e:
        print(e)
        return None