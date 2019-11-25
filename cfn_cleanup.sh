. ./WpeConfig.sh
echo "removing bucket and contents" ${S3_BUCKET}
aws s3 rm s3://${S3_BUCKET}/${WPE_LAMBDA_ZIP}
aws s3 rm s3://${S3_BUCKET}
