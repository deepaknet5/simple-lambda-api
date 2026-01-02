# Simple AWS Lambda API

Minimal Python AWS Lambda API using API Gateway (Lambda Proxy).

## Endpoints

### GET /health
Returns service health.

### GET /hello?name=YourName
Returns a greeting.

### POST /echo
Echoes JSON body.

## Deployment

1. Zip the files:
   zip -r function.zip handler.py requirements.txt

2. Create Lambda:
   - Runtime: Python 3.10
   - Handler: handler.lambda_handler

3. Attach API Gateway:
   - REST API or HTTP API
   - Enable Lambda Proxy Integration

4. Deploy API Gateway

Done.
