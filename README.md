# Weather API


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
- Get async task working using weather api
- Parse city name to see if it is in list of cities (or just has no numbers in) using flask preprocessing
- Look at celery or rabbitmq for the get weather for cities task 
- Change the models to handle city instead of letter, change the history table to this
- Look at sqlalchemy flush and find a way to reduce the number of db commits
- Find some way to mock for intergration tests
- Find some way to e2e
- Add user and find ways to save favourite cities
- Get the docker compose working, there is a Redis connection error but the letter/id route works fine or use rabitmq
- Create a front-end to show letter, letters