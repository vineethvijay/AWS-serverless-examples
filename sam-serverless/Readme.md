### Steps

1. Create the bucket
2. sam package   --template-file template.yml   --output-template-file package.yml   --s3-bucket sam-serverless-2
3. sam deploy   --template-file package.yml   --stack-name sam-hello-world   --capabilities CAPABILITY_IAM