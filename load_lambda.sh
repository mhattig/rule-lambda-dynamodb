lambda_func=wpe_lambda
echo ${lambda_func}
cd ./${lambda_func}
#rm -f ${lambda_func}.zip
#cd ./package
#zip -r9 ${OLDPWD}/${lambda_func}.zip .
#cd $OLDPWD
zip ${lambda_func}.zip *.py
aws lambda update-function-code --function-name ${lambda_func} --zip-file fileb://${lambda_func}.zip
cd ..
