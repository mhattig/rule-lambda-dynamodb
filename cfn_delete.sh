#!/bin/bash
# file: deploy.sh
set -e

echo "Delete WPE Cloudformation Stack"
aws cloudformation delete-stack \
  --stack-name WpeStack 
