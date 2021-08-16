import pulumi_fastly as fastly

service = fastly.Servicev1(
  "my-service",
  activate=True,
  backends=[{
    "address": "origin.myservice.com",
    "name": "localhost",
    "port": 80,
  }],
  domains=[{"name": 'demo.myservice.com'}],
  force_destroy="true",
)
