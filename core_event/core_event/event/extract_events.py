# import rdflib
import requests
# from urllib3.util.retry import Retry
# from rdflib import Graph, Namespace, URIRef
# import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON
from bs4 import BeautifulSoup

endpoint = "https://skynet.coypu.org/wikievents-20160101-20230131/"
sparql = SPARQLWrapper(endpoint)
# checking connection with endpoint (200 status code)
check_response = sparql.query()
if check_response.response.status != 200:
    print("Error: The endpoint returned a status code of", check_response.response.status)
    print("Content:", check_response.response.content)

query = """
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX gn: <http://www.geonames.org/ontology#>
            PREFIX coy: <https://schema.coypu.org/global#>
            PREFIX dcterms: <http://purl.org/dc/terms/>  
            PREFIX schema: <http://schema.org/>

       SELECT DISTINCT ?event ?title ?abstract ?location ?date #?company
            WHERE{
                        ?event  a coy:WikiNews;
                                    coy:isIdentifiedBy ?context;
                                    coy:hasMentionDate ?date.
                        ?event coy:hasTag ?lable.
                        ?context a nif:Context;
              					    # dcterm:source ?source;
                                    nif:isString ?abstract.

                        ?event coy:isOccuringDuring ?parent_event.
                        ?parent_event coy:hasLocation ?location_entity.
                        ?location_entity coy:isIdentifiedBy ?location.
                        ?parent_event rdfs:label ?title.
    					# ?company wdt:P279? wd:Q783794.
                        
            }
            OFFSET 1500
            LIMIT 1000

        """

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

import pandas as pd

# Extract the query result from the dictionary (results)
result_bind = [
                 {
                    "event": result["event"]["value"],
                    "title": result["title"]["value"],
                    "abstract": result["abstract"]["value"],
                    "location": result["location"]["value"],
                    "date": result["date"]["value"],
                    # "company": result["company"]["value"]
                 } 
                 for result in results["results"]["bindings"]
                ]

# print(result_bind)
# Convert the query result to a pandas dataframe
df = pd.DataFrame(result_bind)

# Export the dataframe to an Excel file
df.to_excel("1000_events_from_endpoint.xlsx", index=False)

