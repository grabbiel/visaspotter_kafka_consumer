import os

# Get the AWS access key ID and secret access key from the environment variables.
ACCESS_KEY_ID = os.environ.get("AWS_SQS_ACCESS_KEY")
SECRET_ACCESS_KEY = os.environ.get("AWS_SQS_SECRET_KEY")
DYNAMODB_ACCESS_KEY_ID = os.environ.get("AWS_DYNAMOB_ACCESS_KEY")
DYNAMODB_SECRET_ACCESS_KEY = os.environ.get("AWS_DYNAMODB_SECRET_KEY")


# Get SQS endpoints
AWS_SQS_URL = os.environ.get("AWS_SQS_URL")

# Get SNS topics
AWS_TOPIC_ID_MATCHREVIEW = os.environ.get("AWS_TOPIC_ID_MATCHREVIEW")
AWS_TOPIC_ID_JOBPOSTING = os.environ.get("AWS_TOPIC_ID_JOBPOSTING")


