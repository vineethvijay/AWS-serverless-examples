import json
import urllib2
url = "https://api.datamuse.com/words?rel_rhy=india"
response = urllib2.urlopen(url)
#print (response)
data = response.read()
#print (data)
values = json.loads(data)
print (values)