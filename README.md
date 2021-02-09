# Technical test

#### What I would like to do with more time

- Explore setting and getting the la poste api key
- Encrypt the la poste api key properly 
- Look at celery and rabbitmq for the get all letters task 
- Find a way to buffer the query all from sql alchemy in case of millions of results 
- Post to AWS Fargate (not doing this because of the laposte sandbox key which needs updating often)
- Look at more testing in Flask and PyTest, previously I've only used unittest
- Get the docker compose working, there is a Redis connection error but the letter/id route works fine

#### Setup

- Install python 3.7 & pipenv
- `pipenv install` to install project's requirements

#### Run

- `pipenv shell` to enter virtual environment (loading the variables in .env)
- `flask run`

#### Explore DB

Database is running on SQLite, it can be browsed using "DB Browser for SQLite" for instance

#### Expected work

1. Connect to La Poste API (https://developer.laposte.fr/) DONE
2. Create an endpoint that fetch the status of a given letter on the La Poste API, and update it in the database DONE
3. Create an endpoint that fetch the status of all letters on the La Poste API, and update it in the database DONE
4. Make previous endpoint respond instantly, and launch an asynchronous task that update all the status DONE

#### Bonus

- Unit, integration, E2E tests
- Store the status history of each letter in a new table
- Impress us
