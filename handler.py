import json


def response(status_code: int, body: dict):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",  # enable CORS
        },
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    """
    AWS Lambda entry point
    Compatible with API Gateway (Lambda Proxy Integration)
    """

    http_method = event.get("httpMethod", "")
    path = event.get("path", "")

    # Health check
    if http_method == "GET" and path == "/health":
        return response(200, {"status": "ok"})

    # Example GET endpoint
    if http_method == "GET" and path == "/hello":
        name = (
            event.get("queryStringParameters", {}) or {}
        ).get("name", "world")

        return response(200, {
            "message": f"Hello, {name}!"
        })

    # Example POST endpoint
    if http_method == "POST" and path == "/echo":
        body = event.get("body")
        try:
            body_json = json.loads(body) if body else {}
        except json.JSONDecodeError:
            return response(400, {"error": "Invalid JSON"})

        return response(200, {
            "you_sent": body_json
        })

    # Not found
    return response(404, {
        "error": "Route not found",
        "method": http_method,
        "path": path,
    })
