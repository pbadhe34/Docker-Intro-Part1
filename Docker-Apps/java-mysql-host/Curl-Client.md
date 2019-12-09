#API available
#Get http://ip:8090/users
#Get http://ip:8090/user/{username}
#Get http://ip:8090/sampleUser
#Post http://ip:8090/user
#Put http://ip:8090/user/
#Delete http://ip:8090/user/{userid}

curl -d "@data.json" -X POST http://localhost:8090/user


curl -d "@data.json"  -H "Content-Type: application/json" -X POST http://192.168.99.100:8090/user


 data.json
{
"firstName":"Baba","lastName":"Zero","userName":"nove"
}

To get all records
curl http://192.168.99.100:8090/users

 To update record

curl -d "@data.json"  -H "Content-Type: application/json"  -x PUT http://localhost:8090/user

 To delete the record

curl -X DELETE http://192.168.99.100:8090/user/{userid}
 

 
 

 
 data.txt
param1=value1&param2=value2
 package.json
{
  "name": "postdemo",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "body-parser": "^1.15.0",
    "express": "^4.13.4"
  }
}