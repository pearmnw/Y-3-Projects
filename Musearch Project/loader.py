import csv
from elasticsearch import Elasticsearch

elas = Elasticsearch(
    "https://localhost:9200",
    ca_certs="/Users/user/Desktop/IR/Project_phase2/ElasticSearchLecture/elasticsearch-8.5.0/config/certs/http_ca.crt",
    basic_auth=("elastic", "Pear2545")
)

print(f"Connected to Elasticsearch cluster `{elas.info().body['cluster_name']}`")

# TODO: read music dataset files
with open("C:/Users/user/Desktop/IR/Project phase 2/Coding/dataset/musicdataset.csv", "r") as f:
    reader = csv.reader(f)

    for i, line in enumerate(reader):
        document = {
            #  "music_id": line[0],
             "music_name": line[0],
             "music_artist": line[1],
             "music_track": line[2],
             "music_genre": line[3],
             "music_release": line[4],
             "music_producer": line[5],
             "music_writer": line[6],
             "music_lyrics": line[7]
        }
        elas.index(index="musicdata", document=document)