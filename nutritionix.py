import requests
import sensitiveData


class Nutritionix:

    trackApiUrl = "https://trackapi.nutritionix.com/v2/natural/exercise"
    query = "ran 3 miles"
    params = {
        "query": query,
        "gender": "male",
        "weight_kg": 70.0,
        "height_cm": 170.0,
        "age": 32
    }
    headers = {
        "x-app-id": sensitiveData.nutritionixAppId,
        "x-app-key": sensitiveData.nutritionixApiKey,
        "Content-Type": "application/json"
    }

    def __init__(self):
        pass

    def setParams(self, query):
        self.params = {
        "query": query,
        "gender": "male",
        "weight_kg": 70.0,
        "height_cm": 170.0,
        "age": 32
    }

    def apiCall(self):
        response = requests.post(url=self.trackApiUrl, json=self.params, headers=self.headers)
        return response.json()["exercises"]
