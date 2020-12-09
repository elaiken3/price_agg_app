
from googleapiclient.discovery import build
import pandas as pd
import config

api_key = config.api_key
cse_id = config.cse_id

#Google Query Function
def google_query(query, api_key, cse_id, **kwargs):
    query_service = build("customsearch",
                          "v1",
                          developerKey=api_key
                          )
    query_results = query_service.cse().list(q=query,    # Query
                                             cx=cse_id,  # CSE ID
                                             **kwargs
                                             ).execute()

    return query_results['items']
#End of Function


#Instantiating lists to hold query elements
my_results_list_link = []
my_results_list_title=[]
my_results_list_snippet=[]


#External input for query
query_name = str(input("Enter Search Name: "))


#Calling Google Query Function with external input for query
my_results = google_query(query_name,
                          api_key,
                          cse_id,
                          num = 10
                          )

#Looping through lists and printing results
for result in my_results:
    my_results_list_title.append(result['title'])
    my_results_list_link.append(result['link'])
    my_results_list_snippet.append(result['snippet'])

    print(result['title'],result['link'],result['snippet'])
