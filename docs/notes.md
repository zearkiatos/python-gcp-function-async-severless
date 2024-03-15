# GCP data storage how to send event from database trigger

## Create event from cloud storage
```sh
# Create function
# gcloud functions deploy function-create-heroe-greet --entry-point load --runtime python39 --trigger-resource <BUCKET_NAME> --trigger-event google.storage.object.finalize --memory 128M --region us-central1 --timeout 60 --min-instances 0 --max-instances 1
$ gcloud functions deploy function-create-heroe-greet --entry-point load --runtime python39 --trigger-resource function-storage-caprilespe --trigger-event google.storage.object.finalize --memory 128M --region us-central1 --timeout 60 --min-instances 0 --max-instances 1
```