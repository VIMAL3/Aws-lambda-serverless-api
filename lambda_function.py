import json

def lambda_handler(event, context):
    query_params = event.get("queryStringParameters") or {}
    name = query_params.get("name", "Cloud Intern")

    body = {
        "message": f"Hello, {name}! Serverless API running on AWS Lambda + API Gateway.",
        "service": "AWS Lambda & API Gateway",
        "status": "200 OK"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
