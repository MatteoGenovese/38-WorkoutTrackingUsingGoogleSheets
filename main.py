import requests
import nutritionix
import sensitiveData
import sheety
from datetime import datetime

nutritionixApi = nutritionix.Nutritionix()
trackSomething = input("Tell me the activities that you have done today")
nutritionixApi.setParams(trackSomething)
response = nutritionixApi.apiCall()
# print(response[0])


sheetyApi = sheety.Sheety()

for sheetInput in response:
    # sheetyApi.getAllTheLine()
    todayDate = datetime.now().strftime("%d/%m/%Y")
    nowTime = datetime.now().strftime("%X")
    exercise = sheetInput["name"]
    duration = int(sheetInput["duration_min"])
    calories = int(sheetInput["nf_calories"])

    print(todayDate, nowTime, exercise, duration, calories)
    sheetyApi.writeData(todayDate, nowTime, exercise, duration, calories)


