# Technical test


#### To run
- install redis redis-server /usr/local/etc/redis.conf
- run redis default port (6379)
- activate virutal env 
- $ pip install 
- $ rq worker  
(in root)
- $ flask run 
(in root)

#### To do
- Change from laposte api to weather api
- Parse the letter ID using flask pre processing of endpoint input (look in tech with tim video and remove static method)
- Make the task properly asynchronous
- Look at celery and rabbitmq for the get all letters task 
- Find a way to buffer the query all from sql alchemy in case of millions of results 
- Look at more testing in Flask and PyTest, previously I've only used unittest
- Get the docker compose working, there is a Redis connection error but the letter/id route works fine or use rabitmq
- Create a front-end to show letter, letters