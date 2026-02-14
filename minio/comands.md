```bash
helm install --set resources.requests.memory=512Mi --set replicas=1 --set persistence.enabled=false --set mode=standalone --set rootUser=admin,rootPassword=admin --generate-name minio/minio
```