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
8. Navigate to AWS IAM
9. Select `Roles`
10. Select `lambdaftp-role-[id]`
11. Select the policy name and edit the JSON
12. Paste IAM.json contents and save
13. Navigate back to Lambda and select lambdaftp
14. Select `code` -> Upload from -> `.zip file`
15. Deploy