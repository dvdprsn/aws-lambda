## lambda FTP

- Set region to CA-Central

1. Navigate to AWS Lambda console page
2. Click `Create function`
3. Function name -> `lambdaftp`
4. Runtime -> `Python 3.9`
5. Click `Create function`
6. Click `Add trigger`
7. Select `API Gateway`
   - Create a new API
   - HTTP API
   - Security Open
8. Configuration -> Permissions -> Click the execution role
9. Add permissions -> attach policies -> add`AmazonS3FullAccess`
10. Back in the lambda function select `code` -> Upload from -> `.zip file`
11. Deploy

Trigger function with -> `https://[API Gateway]/default/lambdaftp?Bucket=[bucket name]&filename=[file name]`
