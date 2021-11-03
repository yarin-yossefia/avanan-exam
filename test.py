

import requests
text= {'log':'yarin'}

resp=requests.put('http://localhost:9200/shay')
#jso= {
#  "name": "national-parks-demo"
#}
#resp = requests.post('http://localhost:9200/api/as/v1/engines/yarin/logs/api',text,headers={'content-type':'application/json', 'charset':'UTF-8'})
#resp = requests.post('http://localhost:9200/api/as/v1/engines', jso,headers={'content-type':'application/json', 'charset':'UTF-8'})
#resp = curl -X GET 'http://localhost:9200/api/as/v1/engines/[ENGINE]/logs/api'  \
#        -H 'Content-Type: application/json'
print (resp.content)
