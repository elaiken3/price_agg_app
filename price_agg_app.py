
from googleapiclient.discovery import build
import pandas as pd
import config
import sys
sys.executable

api_key = config.api_key
cse_id = config.cse_id

#Google Query Function
def google_query(item, api_key, cse_id, **kwargs):
    df = pd.read_excel('./'+file)
    df['Product_Name'] = df['Main Vendor'] + ' ' + df['Description']
    item_list=[]
    for item in df['Product_Name']:
        item.append(df['Product_Name'])


    query_service = build("customsearch",
                          "v1",
                          developerKey=api_key
                          )
    for item in item_list:
        query_results = query_service.cse().list(q=item,    # Query
                                             cx=cse_id,  # CSE ID
                                             **kwargs
                                             ).execute()

        print(query_results['items'])
        return query_results['items']

#End of Function


#Instantiating lists to hold query elements
my_results_list_link = []
my_results_list_title=[]
my_results_list_snippet=[]


#External input for query
file = str(input("Enter File Name:"))


#Calling Google Query Function with external input for query
my_results = google_query(file,
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
