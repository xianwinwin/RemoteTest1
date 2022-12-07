from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import pandas as pd

#https://dylancastillo.co/elasticsearch-python/
#pip install elasticsearch==8.3.3

def get_df():
    
    file_path = "/Users/macbook/Desktop/wiki_movie_plots_deduped.csv"
    file_path = 'I:\\My Drive\\GAS_VISTA_SHARED\\easy_transfer\\wiki_movie_plots_deduped.csv'

    df = (
        pd.read_csv(file_path)
        .dropna()
        .sample(5000, random_state=42)
        .reset_index()
    )
    
    return df

def ping_es():
    es = Elasticsearch("http://log-n.com:9200")
    print (es.info().body)
    return es

def create_es():
    es = Elasticsearch("http://log-n.com:9200")
    
    mappings = {
        "properties": {
            "title": {"type": "text", "analyzer": "english"},
            "ethnicity": {"type": "text", "analyzer": "standard"},
            "director": {"type": "text", "analyzer": "standard"},
            "cast": {"type": "text", "analyzer": "standard"},
            "genre": {"type": "text", "analyzer": "standard"},
            "plot": {"type": "text", "analyzer": "english"},
            "year": {"type": "integer"},
            "wiki_page": {"type": "keyword"}
        }
    }

    es.indices.create(index="movies", mappings=mappings)
    return es


def bulk_entry(es, df):
        
    bulk_data = []
    for i,row in df.iterrows():
        bulk_data.append(
            {
                "_index": "movies",
                "_id": i,
                "_source": {        
                    "title": row["Title"],
                    "ethnicity": row["Origin/Ethnicity"],
                    "director": row["Director"],
                    "cast": row["Cast"],
                    "genre": row["Genre"],
                    "plot": row["Plot"],
                    "year": row["Release Year"],
                    "wiki_page": row["Wiki Page"],
                }
            }
        )
    bulk(es, bulk_data)

def count_items(es):
    es.indices.refresh(index="movies")
    r = es.cat.count(index="movies", format="json")
    print (r)


def search(es):
    resp = es.search(
    index="movies",
    body={
        "query": {
            "bool": {
                "must": {
                    "match_phrase": {
                        "cast": "jack nicholson",
                    }
                },
                "filter": {"bool": {"must_not": {"match_phrase": {"director": "roman polanski"}}}},
            },
            },            
        }
    )
    return resp

def query(es):
    
    directors = ["D. W. Griffith","Thomas H. Ince","Cecil B. DeMille"]
 
    es_query = {
                "bool": {
                            "must": {
                                        "match": { "director": 'Thomas H. Ince' },
                                        "match": { "year": 1993 },                                        
                                    }
                        }
                }
                 
    res = es.search(index="movies", query=es_query)    
    return res['hits']['hits']

def f1():
    es = ping_es()
    create_es()
    df = get_df()
    bulk_entry(es, df)
    count_items(es)
    response = search(es)
    print (response)


def f2():
    es = ping_es()
    count_items(es)
    print ("*"*32)
    res = query(es)
    for i,r in enumerate(res):
        print (i+1,r['_score'],r['_source']['title'])


if __name__=='__main__':
    print ("start...")
    f2()
    print ("END")