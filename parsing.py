from pprint import pprint

import requests
import json

def get_service():
    hh_info = requests.get("https://api.hh.ru/vacancies")
    return hh_info.text

# pprint(get_service())



def get_service_job():
    job_info = requests.get("https://api.superjob.ru/2.0/vacancies",headers={"X-Api-App-Id": "v3.r.137645209.b47468e74b48a5fb3a8923a38104bf7bf9405bc5.c332503b8cc95ce4034c399dae34c4042e4a09bc"})
    return job_info.text

print(get_service_job())