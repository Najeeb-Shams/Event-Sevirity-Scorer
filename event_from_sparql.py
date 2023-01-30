# import rdflib
import requests
# from urllib3.util.retry import Retry
# from rdflib import Graph, Namespace, URIRef
# import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON
from bs4 import BeautifulSoup

endpoint = "https://skynet.coypu.org/wikievents-20160101-20221130/"
sparql = SPARQLWrapper(endpoint)
# code for checking connection with endpoint (200 status code)
check_response = sparql.query()
if check_response.response.status != 200:
    print("Error: The endpoint returned a status code of", check_response.response.status)
    print("Content:", check_response.response.content)

query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX coy: <https://schema.coypu.org/global#>

            SELECT ?event ?raw_html ?ev_place ?ev_st_date
                WHERE { 
                     ?event a coy:WikiNews .
                        ?event coy:hasRawHtml ?raw_html .
                        ?event coy:hasLocation ?location . # used for accessing the event_place
                        ?location coy:isIdentifiedBy ?ev_place .
                        ?event coy:hasTimespan ?timespan . # used in the following line for accessing the start date of a event (indirect
                        ?timespan  coy:hasStartDate ?ev_st_date.               
                } 
            OFFSET 1127
            LIMIT 2
        """

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

events_list = {
    "event1": {"text": "abc", "place": "New York", "date": "2022-01-01"},
    "event2": {"text": "xyz", "place": "London", "date": "2022-02-01"}
}     
count=1 
for result in results["results"]["bindings"]:
    raw_html = result["raw_html"]["value"]
    ev_place = result["ev_place"]["value"]
    ev_start_date = result["ev_st_date"]["value"]
        # Removing HTML_tags from the SPARQL response raw_HTML
    # clean_raw_html = raw_html
    soup = BeautifulSoup(raw_html, 'html.parser')
    event_text = soup.get_text()
    values ={'text':event_text, 'place':ev_place, 'date':ev_start_date}
    if count ==1:
        events_list['event1'].update(values)
    elif count==2:    
        events_list['event2'].update(values)
    count +=1
