#!/bin/bash
# deploy app to staging server

echo "Deploying current version to staging server"

fab deploy -i /Users/ZachLiu/OneDrive/AWS/zachliu.aws/re-tools-instance/re-tools-instance-key-pair.pem  --host=ubuntu@dev.real-estate-tools.com
