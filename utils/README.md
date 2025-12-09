## Utility pod that allows easy troubleshooting and testing.

Deploy with:
`kubectl apply -f Deployment_curl.yaml`

Get pod name:
`kubectl get po ....`

Then connect to it:
`kubectl exec -it deployment-curl-5b7c9798b4-mgbr6 -- sh`

Run requests to gateway service in a loop:
`/app # while true; do curl  dydemo-gateway-service.default.svc.cluster.local/latency; done`
