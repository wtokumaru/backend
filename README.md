# ChronoScio Backend [![Build Status](https://travis-ci.org/chronoscio/backend.svg?branch=master)](https://travis-ci.org/interactivemap/backend) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/0074e97bc13b476ea3eec279483d3cab)](https://www.codacy.com/app/whirish/backend?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=interactivemap/backend&amp;utm_campaign=Badge_Grade)

## Getting Started
We normally use [Docker](https://en.wikipedia.org/wiki/Docker_(software)) to simplify installation and configuration. Docker makes virtual "containers" as images which allow us to isolate code we run and work around computer-specific weirdnesses. Docker should work on [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/) or [macOS](https://docs.docker.com/docker-for-mac/install/) but requires Hyper-V, which is not available on Windows 10 Home edition. If you have trouble with setting up Docker, see the **Local Development** instructions below instead. Otherwise, it should be simple to get started:
```bash
# Clone the repo
git clone https://github.com/chronoscio/backend

# Create env files, remember to update accordingly
mv django.env.sample django.env
mv postgres.env.sample postgres.env

# Build and start the docker containers
make run

# Navigate to http://localhost/, if you get a 502 error postgres likely has not been initialized yet,
#   try again in a few seconds
```

## Local Development
1) Create a python virtualenv, activate it, and install the package requirements:
```bash
# Clone the repo if you have not already.
git clone https://github.com/chronoscio/backend

# Navigate to the backend repo.
cd backend

# Begin a virtual environmnet.
virtualenv venv

# Activate the virtual environment.
source venv/bin/activate

# Install the project requirements manually.
pip install -r config/requirements.txt
```
2) Install and run [Postgresql](https://www.postgresql.org/docs/9.3/static/tutorial-install.html) (AKA postgres) locally. You should not need to worry about creating any accounts or doing any setup but you may need to debug OS-specific problems that appear. For example, you may need to install postgis as well. (TODO: Test this on wiped setups to find out specific steps to do this properly.)
3) Change the HOST variable in the [settings.py](https://github.com/chronoscio/backend/blob/master/project/interactivemap/settings.py) file to be `localhost` instead of `db`. You may also need to change the PORT variable to match whatever you have set for postgis (TODO: investigate this).
4) Prepare a json dataset fto be the database. For now, you can use our example test data.
```bash
mv docs/example_db_dump.json project/db.json
```

5) Migrate and run the server with django.
```bash
# Migrate the project.
python project/manage.py migrate

# Run the server.
python3 project/manage.py runserver
```

## Contributing
Please refer to the [developer guide](./docs/DEVELOPER.md) and [contribution guide](./docs/CONTRIBUTING.md) to learn how the backend is structured.

## Architecture
config: Configuration files and requirements.

docs: Documentation and example database.

project/api/migrations: Auto-generated migration classes?

project/api: REST API and a test file (how/why do we run the test)?  Defines the Nation, Territory, and DiplomaticRelation classes, which are our primary database items.

project/interactivemap: Django settings and website directory layout?

project: Django execution wrapper.
