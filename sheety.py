import requests
import json
import sensitiveData


class Sheety:
    url = 'https://api.sheety.co/5a32935d1369e5600961110acebc25f6/workout/workouts'
    headers = {
        "Authorization": f"Bearer {sensitiveData.bearTokenSheety}"
    }

    def getAllTheLine(self):
        response = requests.get(self.url)
        json_data = response.json()
        # Do something with the data
        print(f"given: \n{json_data['workouts']}")
        return json_data['workouts']

    def writeData(self, date, time, exercise, duration, calories):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {sensitiveData.bearTokenSheety}"
        }
        body = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
        }
        response = requests.post(self.url, json=body)
        json_data = response.json()
        print(json_data)
