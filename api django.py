import requests

from django.http import JsonResponse

def get_users(requst):
    url = ""
    response = requests.get(url , timeout=10)
    response.raise_for_status()
    data = response.json()

    return JsonResponse(data , safe= False)