### Steps

1. Create the bucket
2. sam package   --template-file template.yml   --output-template-file package.yml   --s3-bucket serverless-sam-bucket1
3. sam deploy   --template-file package.yml   --stack-name sam-hello-world   --capabilities CAPABILITY_IAM
4. aws cloudformation delete-stack --stack-name sam-hello-world

### Local testing

1. sam local start-api