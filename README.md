# ATM tellel machine graphql endpoint for rabbitmq server
Exercise for the distributed programming course in university of macedonia

## Python3.10.8 dependences 
read requirments.txt
  
## Usage
Given that you have access to the rabbitmq server just change the ip and port in main.py AtmHost AtmPort so it points to the rabbitmq queue and then start it up with```uvicorn main:schema --port 8081```

