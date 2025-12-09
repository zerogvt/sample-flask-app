## Build and Deploy
`docker build . -t dydemo/backend:1.0 && kubectl delete -f Deployment.yaml && kubectl apply -f Deployment.yaml`


## Run dev server
`. ../venv/bin/activate`
`env FLASK_APP=backend.py python -m flask run`
