## run flask app
Reuse the local  daemon from Minikube with 
`eval $(minikube docker-env)`

Build & Run:
`docker build . -t flask/flask.app:2.2 && k delete -f Deployment.yaml && k apply -f Deployment.yaml`


## install dynatrace
 `kubectl delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.7.2/kubernetes-csi.yaml`

 `kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.7.2/kubernetes-csi.yaml`

 `kubectl apply -f dynatrace.yaml`
