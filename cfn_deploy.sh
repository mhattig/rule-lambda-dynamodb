#!/bin/bash
# file: deploy.sh
set -e

. ./cfn_config.sh

aws s3 cp ${WPE_LAMBDA}/${WPE_LAMBDA_ZIP} s3://${S3_BUCKET}

echo "Deploy WPE Cloudformation"
aws cloudformation deploy \
  --template-file cfn_wpe.json \
  --parameter-overrides \
WpeRuleName=${WPE_RULE} \
WpeLambdaRoleName=${WPE_LAMBDA_ROLE} \
WpeLambdaName=${WPE_LAMBDA} \
S3BucketName=${S3_BUCKET} \
WpeLambdaZipName=${WPE_LAMBDA_ZIP} \
WpeDynamoDbName=${WPE_DYNAMODB} \
  --stack-name WpeStack \
  --capabilities CAPABILITY_NAMED_IAM

