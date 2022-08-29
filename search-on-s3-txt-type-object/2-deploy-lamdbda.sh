#!/bin/bash

virtualenv lambda_venv
source lambda_venv/bin/activate
pip install smart_open
pip install boto3
pip freeze > requirements.txt

cd lambda_venv/lib/python*/sit*
zip -r9 ${OLDPWD}/lambda.zip .
cd $OLDPWD
zip -g lambda.zip lambda_function.py 