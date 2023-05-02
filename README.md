# python-boilerplate

Python project with FastAPI with server to be able to use as base for other projects


## To Run

Create a new enviroment with pyenv(or similar):
```
virtualenv .venv;source .venv/bin/activate
```

Install all dependencies:
```
make install
``` 

run project:
```
make run
```

Features:

- [x] Fastapi server
- [x] Env(envExample) to configura Enviroments
- [x] Rocketry Scheduler
- [x] Health Endpoint
- [x] "Config Path" in app
- [x] Docker-Compose file to test connections (in future with RabbtiMQ - MongoDB)
- [x] Docker File to Python
- [x] Makefile
- [ ] CRUD Mongo Repository
- [ ] CRUD with MONGO DB to Products
- [ ] K8S file to implementation
