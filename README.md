# ChronoScio Backend [![Build Status](https://travis-ci.org/chronoscio/backend.svg?branch=master)](https://travis-ci.org/interactivemap/backend) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/0074e97bc13b476ea3eec279483d3cab)](https://www.codacy.com/app/whirish/backend?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=interactivemap/backend&amp;utm_campaign=Badge_Grade)

## Getting Started
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

## Contributing
Please refer to the [developer guide](./docs/DEVELOPER.md) and [contribution guide](./docs/CONTRIBUTING.md) to learn how the backend is structured.

## Architecture
config: Configuration files and requirements.

docs: Documentation and example database.

project/api/migrations: Auto-generated migration classes?

project/api: REST API and a test file (how/why do we run the test)?  Defines the Nation, Territory, and DiplomaticRelation classes, which are our primary database items.

project/interactivemap: Django settings and website directory layout?

project: Django execution wrapper.
