@echo off
echo ==============================================
echo  Deploying 'send-cv' to GCP Project: junyi-personal-page
echo ==============================================

gcloud functions deploy send-cv ^
    --gen2 ^
    --runtime=python311 ^
    --region=europe-west1 ^
    --source=. ^
    --entry-point=send_cv ^
    --trigger-http ^
    --allow-unauthenticated ^
    --env-vars-file=env.yaml ^
    --project=junyi-personal-page

echo.
echo ==============================================
echo  Deployment Complete!
echo  Check the URL above to test.
echo ==============================================
pause