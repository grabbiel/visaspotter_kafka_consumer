# pip imports
import boto3
import sys
import os
import botocore.client


# set import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# local modules: variables
from config.aws import ACCESS_KEY_ID
from config.aws import SECRET_ACCESS_KEY
from config.aws import DYNAMODB_ACCESS_KEY_ID
from config.aws import DYNAMODB_SECRET_ACCESS_KEY


def get_sqs_client() -> botocore.client :
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        region_name='us-east-2'
    )
    sqs_client = session.client("sqs", region_name='us-east-2')
    return sqs_client

def get_dynamodb_client() -> botocore.client:
    session = boto3.Session(
        aws_access_key_id=DYNAMODB_ACCESS_KEY_ID,
        aws_secret_access_key=DYNAMODB_SECRET_ACCESS_KEY,
        region_name="us-east-2"
    )
    dynamodb_client = session.resource('dynamodb', region_name='us-east-2')
    return dynamodb_client