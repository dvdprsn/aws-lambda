# Subscribe Deployment

- Create a bucket to serve as the 'hub'
  - Create a folder `dist/` -> anything uploaded here will trigger the function (Keeps it clean)
- Modify sub_list.json to include user and related bucket names -> ensure these buckets exist
- Upload `log.txt` and `sub_list.json` to the 'hub' buckets root

## Create and push container image to ECR

1. Navigate to AWS ECR
2. Create a (or use an existing) private container repo
3. Select the new repo -> `View push commands` -> follow these steps within the local project directory
4. Verify the container is pushed to ECR

## Deploy Container

1. Navigate to AWS lambda console page
2. `Create function`-> from `Container Image` -> Enter the container URI and `Create function`
3. Click `add trigger` -> `S3` -> select the 'hub' bucket -> add `dist/` prefix
4. `Configuration` -> `Permissions` -> Click execution role
5. `Add permissions` -> `Attach policies` -> `AmazonS3FullAccess` -> save
