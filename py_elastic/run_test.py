from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import pandas as pd

#https://dylancastillo.co/elasticsearch-python/
#pip install elasticsearch==7.17.7

def read_data():
    es = Elasticsearch("http://localhost:9200")
    
    df = (
        pd.read_csv("/Users/macbook/Desktop/wiki_movie_plots_deduped.csv")
        .dropna()
        .sample(5000, random_state=42)
        .reset_index()
    )
    
    print (df.head())

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

    #es.indices.create(index="movies", mappings=mappings)
    
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
    
    
if __name__=='__main__':
    print ("start...")
    read_data() 
    print ("END")