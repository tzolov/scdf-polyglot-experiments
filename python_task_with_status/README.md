
Build docker image and push to Docker Hub. Note: replace `tzolov` with your docker hub prefix.
```bash
docker build -t tzolov/python_task_with_status:0.1 .
docker push tzolov/python_task_with_status:0.1
```

Register the docker image as SCDF task

```bash
dataflow:>app register --type task  --name python-task-with-status --uri docker://tzolov/python_task_with_status:0.1
dataflow:>task create --name python-task --definition "python-task-with-status"
dataflow:>task launch --name python-task
```