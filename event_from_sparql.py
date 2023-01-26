# import rdflib
# import requests
# from urllib3.util.retry import Retry
# from rdflib import Graph, Namespace, URIRef
# import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint = "https://skynet.coypu.org/wikievents-20160101-20221130/"
sparql = SPARQLWrapper(endpoint)
query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX coy: <https://schema.coypu.org/global#>
            SELECT ?event ?raw_html
            WHERE { 
                ?event a coy:WikiNews .
                ?event coy:hasRawHtml ?raw_html .	                
            } 
            OFFSET 1000
            LIMIT 1
        """

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    # event = result["event"]["value"]
    raw_html = result["raw_html"]["value"]
    # print(f"Event: {event}\nRaw HTML: {raw_html}\n")
    print(f"Raw HTML: {raw_html}\n")



# codes for debuging the endpoint
# import json
# session = requests.Session()
# session.max_redirects = 0
# headers = {'Accept': 'application/sparql-results+json'}
# response = session.post(endpoint, data=query, headers=headers)
# if response.headers["content-type"] != "application/sparql-results+json":
#     print("Error: The endpoint did not return JSON results")
#     print("Content-Type:", response.headers["content-type"])
#     print("Content:", response.content)
# else:
#     results = json.loads(response.text)
#     for result in results["results"]["bindings"]:
#         event = result["event"]["value"]
#         print(f"Event: {event}\n")

# #code for checking endpoint response return format
# response = sparql.query()
# if response.response.headers["content-type"] != "application/sparql-results+json":
#     print("Error: The endpoint did not return JSON results")
#     print("Content-Type:", response.response.headers["content-type"])
# else:
#     results = response.convert()
#     for result in results["results"]["bindings"]:
#         event = result["event"]["value"]
#         print(f"Event: {event}\n")


# code for checking connection with endpoint (200 status code)
# response = sparql.query()
# if response.response.status != 200:
#     print("Error: The endpoint returned a status code of", response.response.status)
#     print("Content:", response.response.content)
# else:
#     results = response.convert()
#     for result in results["results"]["bindings"]:
#         event = result["event"]["value"]
#         print(f"Event: {event}\n")
