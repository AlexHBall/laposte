# Technical test


#### To run

- run redis default port (6379)
- activate virutal env 
- $ pip install 
- $ rq worker  
(in root)
- $ flask run 
(in root)

#### What I would like to do with more time

- Explore setting and getting the la poste api key
- Encrypt the la poste api key properly 
- Look at celery and rabbitmq for the get all letters task 
- Find a way to buffer the query all from sql alchemy in case of millions of results 
- Post to AWS Fargate (not doing this because of the laposte sandbox key which needs updating often)
- Look at more testing in Flask and PyTest, previously I've only used unittest
- Get the docker compose working, there is a Redis connection error but the letter/id route works fine