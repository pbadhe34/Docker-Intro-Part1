from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
#redis = Redis(host="redis", db=0, socket_connect_timeout=2, #socket_timeout=2)

//Read the env varaiabloe pointing to Redishost ip address

redisHost = os.getenv("Redis-host","redis-server")


//redis = Redis(host='redis', port=6379)

//connect to the redis-server IP 

redis = Redis(host={redisHost}, port=6379)



app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    print 'Content-type: text/html\n\n'

    uname = os.getenv("NAME","world")
     
    host = socket.gethostname()     
    
    hostAddr = socket.gethostbyname(socket.gethostname())     

        
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Host-Address:</b>{hostip}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=uname, hostname=host,hostip=hostAddr,visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)
