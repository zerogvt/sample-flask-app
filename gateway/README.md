## Build and deploy

`docker build . -t dydemo/gateway:1.0 && kubectl delete -f Deployment.yaml && kubectl apply -f Deployment.yaml`
