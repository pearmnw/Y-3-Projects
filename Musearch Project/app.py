from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
import os 


elas = Elasticsearch(
    "https://localhost:9200",
    ca_certs="/Users/user/Desktop/IR/Project_phase2/ElasticSearchLecture/elasticsearch-8.5.0/config/certs/http_ca.crt",
    basic_auth=("elastic", "Pear2545")
)

print(f"Connected to ElasticSearch cluster `{elas.info().body['cluster_name']}`")

app = Flask(__name__)

MAX_SIZE = 15

@app.route("/")
def home():
    return render_template("index.html")

def formatQuery(searchquery):
    import json
    import pprint
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
    query=nested_dict()
    query['span_near']['clauses']=list()
    query['slop']='1'
    query['in_order']="false"
    words=searchquery.split()
    for w in words:
        nest = nested_dict()
        nest["span_multi"]["match"]["fuzzy"]["msg"]["fuzziness"]["value"] = w
        nest["span_multi"]["match"]["fuzzy"]["msg"]["fuzziness"]["fuzziness"] = "1"
        json.dumps(nest)
        query['span_near']['clauses'].append(json.loads(json.dumps(nest)))

@app.route("/search")
def search_autocomplete():
    query = request.args["q"].lower()
    formatQuery(query)

    new_query = {
        # To search for many fields
        "multi_match": {
            "query": query,
            "fields": [

                "music_name",
                "music_name.trigram",
                "music_name.reverse",

                "music_artist",
                "music_artist.trigram",
                "music_artist.reverse",

                "music_track",
                "music_track.trigram",
                "music_track.reverse",

                "music_genre",
                "music_genre.trigram",
                "music_genre.reverse",

                "music_release",
                "music_release.trigram",
                "music_release.reverse",

                "music_producer",
                "music_producer.trigram",
                "music_producer.reverse",

                "music_writer",
                "music_writer.trigram",
                "music_writer.reverse",

                "music_lyrics",
                "music_lyrics.trigram",
                "music_lyrics.reverse",
                
            ],
            # and Operator
            "operator": "and",
            # To show the data that has many stopword
            "zero_terms_query": "all",
            # Wrong word but can find OwO
            "fuzziness": "AUTO",
            "max_expansions": 50, 
            # Minimum number of clauses that must match for a document to be returned.
            "minimum_should_match": "60%",
            # define the prefix
            "prefix_length": len(query)//2
        }
    }

    resp = elas.search(index="musicdata", query=new_query, size=MAX_SIZE)
    list = [result['_source'] for result in resp['hits']['hits']]
    print(list)
    return jsonify(list)

if __name__ == '__main__':
    app.run(debug=True)