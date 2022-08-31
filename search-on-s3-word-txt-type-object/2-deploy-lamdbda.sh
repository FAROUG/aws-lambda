#!/bin/bash

pip3 install virtualenv
virtualenv lambda_venv
source lambda_venv/bin/activate
pip3 install smart_open
pip3 install boto3
pip3 freeze > requirements.txt

cd lambda_venv/lib/python*/sit*
zip -r9 ${OLDPWD}/lambda.zip .
cd $OLDPWD
zip -g lambda.zip lambda_function.py 