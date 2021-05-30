import requests,json

api = "http://api.open-notify.org/astros.json"

print(api)

r = requests.get(url=api)
if r.status_code == 200:
        print("success")
        r_text = r.text
        r_json = json.loads(r_text)

length = len(r_json[u'people'])

name_list = []
for i in range(length):
#        print(r_json[u'people'][i][u'name'])
        name_list.insert(i, r_json[u'people'][i][u'name'])

name_list.sort()

print(name_list)
