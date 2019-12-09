from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    print 'Content-type: text/html\n\n'
    uname = os.getenv("NAME","world")
    print "Name is "

    print uname   
   

    host = socket.getfqdn(socket.gethostname())

    print "HostName is "

    print host

    print "Host Address is "
    
    hostAddr = socket.gethostbyname(socket.gethostname())

    print hostAddr
    

        
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b>{hostname}<br/>" \
           "<b>Host-Address:</b>{hostaddr}<br/>" \
           "<b>Visits:</b>{visits}"
    return html.format(name=uname, hostname=host,hostaddr=hostAddr,visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)