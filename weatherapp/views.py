from django.shortcuts import render
import json
import urllib.request
from django.http import Http404

# Create your views here.
def index(request):
    try:
        if request.method=='POST':
            city = request.POST['city']   #the name var in input of index.html is in brackets here
            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8bafe6e7cf39fb53afc4b8eed1d5e632').read()

            json_data = json.loads(res)
            # data={
            #     "country_code":str(json_data['sys']['country']),
            #     "coordinate": str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            #     "temp":str(json_data['main']['temp'])+' k',
            #     "pressure": str(json_data['main']['pressure'])+' pascal',
            #     "humidity": str(json_data['main']['humidity']),
            # }
            
            res2 = urllib.request.urlopen(('https://api.teleport.org/api/urban_areas/slug:{}/images/').format(city)).read()

            json_data2 = json.loads(res2)


            data = {
            "city":city,
            "country_code":str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp":str(int(json_data['main']['temp'])-273)+'c',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
            "image":str(json_data2['photos'][0]['image']['web']),
        }
        
            
            # data2={
            # "image":str(json_data2['photos'][0]['image']['web']),
            # }
                # print(data)
        else:
            data={"city":"h",
                    "country_code":"hhh"   ,"coordinate":"hhhhh",
                    "temp":"w","pressure":"wk","humidity":"ww","image":"jjj"}
                

    except:
        city = request.POST['city']   #the name var in input of index.html is in brackets here
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8bafe6e7cf39fb53afc4b8eed1d5e632').read()

        json_data = json.loads(res)
        data = {
            "city":city,
            "country_code":str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp":str(int(json_data['main']['temp'])-273)+'c',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }
    return render(request, 'index.html',  {"data":data})