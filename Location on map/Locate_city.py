import geopy
import folium
cities,years=[],[]
def locate(file_name):
    for game in open(file_name,'r'):
        city=game.splitlines()
        city=''.join(city)
        cities.append(city)
    geolocator=geopy.geocoders.Nominatim(user_agent='kira')
    m=folium.Map(location=[20,0],tiles='Mapbox Bright',zoom_start=2)
    for city_new in cities:
        print('locating.......'+city_new)
        location=geolocator.geocode(city_new,timeout=10)
        folium.Marker([location.latitude,location.longitude],popup=city_new).add_to(m)
    m.save('locate.html')
