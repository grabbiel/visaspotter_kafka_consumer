# pip install
import sys
import os
import json

# import local modules: variables
from utils.aws_credentials import get_sqs_client
from utils.db_connections import match_review_process, get_cursor, get_dynamodb_table_manager, set_db_connection, put_dynamodb_table_item

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.aws import AWS_SQS_URL
from config.aws import AWS_TOPIC_ID_JOBPOSTING
from config.aws import AWS_TOPIC_ID_MATCHREVIEW
from config.db import DB_DBNAME
from config.db import DB_HOSTNAME
from config.db import DB_PASSWORD
from config.db import DB_USER

def process_topic_messages(topic_arn: str, parser , db_user) -> None:
    sqs_client = get_sqs_client()
    # retrieve response
    response = sqs_client.receive_message(
        QueueUrl=AWS_SQS_URL,
        VisibilityTimeout=30,
        WaitTimeSeconds=20,
        MaxNumberOfMessages=10
    )
    # process messages
    for message in response.get('Messages', []):
        message_body = json.loads(message['Body'])
        attribute_topic_arn = message_body.get('TopicArn')
        print(attribute_topic_arn)
        # skip messages not belonging to a specific SNS topic
        if attribute_topic_arn == topic_arn:
            print("Found topic message")
            # process message
            message_data = json.loads(message_body['Message'])
            parser(db_user, message_data)
            # ... do something with the message data ...
            # decouple queue
            sqs_client.delete_message(
                QueueUrl=AWS_SQS_URL,
                ReceiptHandle=message['ReceiptHandle'],
            )

def process_match_review() -> None:
    conn = set_db_connection(DB_HOSTNAME, 3315, DB_USER, DB_PASSWORD, DB_DBNAME)
    cursor = get_cursor(conn)
    process_topic_messages(AWS_TOPIC_ID_MATCHREVIEW, match_review_process, cursor)
    conn.commit()
    cursor.close()
    conn.close()

def process_job_posting() -> None:
    print("Creating DynamoDB Table manager")
    table_manager = get_dynamodb_table_manager()
    print("Processing messages")
    process_topic_messages(AWS_TOPIC_ID_JOBPOSTING, put_dynamodb_table_item, table_manager)