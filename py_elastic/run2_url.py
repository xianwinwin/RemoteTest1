
import json, requests
import urllib3

#http://log-n.com:9200/_cat/indices?v
#http://log-n.com:9200/movies/_search?q=genre:musical
#more: https://www.bmc.com/blogs/elasticsearch-commands/

http = urllib3.PoolManager()

def test_url():  
    url = 'http://log-n.com:9200'
    resp = http.request('GET', url)
    print(resp.status)
    if resp.status==200:
        print ("CONNECTION OK")
    else:
        print ("CONNECTION FAILED (firewall?!?!)")


def query():    
  
    uri = 'http://log-n.com:9200/movies/_search?q=genre:musical'
    response = requests.get(uri)
    results = json.loads(response.text)
    hits = results['hits']['hits']
    for i,h in enumerate(hits):
        print (i,h['_source']['title'])
    


if __name__=='__main__':
    print ("start...")
    #test_url()
    query()
    print ("END")