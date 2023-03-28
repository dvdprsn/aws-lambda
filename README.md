# Lambda Functions

David Pearson

1050197

dpears04@uoguelph.ca

# How it works

## LambdaFTP

- Very simple function that gets the request from HTTP query string
- Attempts a get_object call based on the string provided
- If file is found the file is returned to the browser as a download

## Subscribe

- Based on the event that triggers the function it will get the bucket name, and file name
- It will then get the list of all subscribers and update the log file indicating which file was uploaded
- It will iterate over the list of subscribers attempting to S3 copy the file into each bucket
- If one of these copies fails it will report to CloudWatch and proceed.

# Deploy instructions

## lambda FTP

- Assumes a valid bucket has been created for FTP

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

## Subscribe Deployment

- Create a bucket to serve as the 'hub'
  - Create a folder `dist/` -> anything uploaded here will trigger the function (Keeps it clean)
- Modify sub_list.json to include user and related bucket names -> ensure these buckets exist
- Upload `log.txt` and `sub_list.json` to the 'hub' buckets root

### Create and push container image to ECR

1. Navigate to AWS ECR
2. Create a (or use an existing) private container repo
3. Select the new repo -> `View push commands` -> follow these steps within the local project directory
4. Verify the container is pushed to ECR

### Deploy Container

1. Navigate to AWS lambda console page
2. `Create function`-> from `Container Image` -> Enter the container URI and `Create function`
3. Click `add trigger` -> `S3` -> select the 'hub' bucket -> add `dist/` prefix
4. `Configuration` -> `Permissions` -> Click execution role
5. `Add permissions` -> `Attach policies` -> `AmazonS3FullAccess` -> save

# Assumptions/Limitations

- All buckets as specified in the instructions must be created (FTP bucket, distribution bucket & related user buckets)
  - For Subscribe this all requires the provided files have been uploaded to the distribution bucket
