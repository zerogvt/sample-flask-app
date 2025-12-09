## Build and deploy

`docker build . -t dydemo/gateway:1.0 && kubectl delete -f Deployment.yaml && kubectl apply -f Deployment.yaml`


## Run dev server
`. ../venv/bin/activate`
`env FLASK_APP=gateway.py python -m flask run --port 8000`
