import requests
import sys
game = sys.argv[1]
param = {'game':game}

req = requests.get('http://127.0.0.1:5000/api/offers',params=param)

print(req.text)

