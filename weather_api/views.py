from django.shortcuts import render
import requests

# Create your views here.
APIkey = "30c3e2eb8c25cd15ad4d371f0d8c619a"

def get_data(request):
    city = request.GET.get('city','mumbai')
    # zip  = request.GET.get('zip','INXX0087')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}"
    data = requests.get(url).json()

    if 'name' in data:
        payload = {
            'weather':data['weather'][0]['main'],
            'temp':int(data["main"]['temp']-273),
            'description':data['weather'][0]['description'],
            'city':data['name']
        }

        context = {
            'data':payload
        }

        return render(request,'weather.html',context)
    
    else:
        context = {
            'data1':"Enter valid city name "
        }

        return render(request,'weather.html',context)

