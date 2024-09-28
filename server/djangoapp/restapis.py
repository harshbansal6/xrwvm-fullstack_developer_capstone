# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv
import requests

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://127.0.0.1:3030")

searchcars_url = os.getenv(
    'searchcars_url', default="http://127.0.0.1:3050")

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

print(searchcars_url)
def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    
    request_url = backend_url + endpoint + "?" + params.rstrip('&')

    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None

def searchcars_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    
    request_url = searchcars_url + endpoint + "?" + params.rstrip('&')

    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None
# Add code for get requests to back end

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments

# def post_review(data_dict):
# Add code for posting review
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")