#One night build for the github 
import requests 
import os
from PIL import Image
from io import BytesIO


filename = str(input("Enter the filename :  "))
longitude = float(input('Enter Longitude : '))
latitude = float(input('Enter latitude : '))


# test data 

# filename = "nyc.png"
# lat, lon = 40.7128, -74.0060


# get the image using an open aerial map api 

def getImage(lat, lon):
    search_url = f"https://api.openaerialmap.org/meta?bbox={lon-0.1},{lat-0.1},{lon+0.1},{lat+0.1}&limit=1"
    response = requests.get(search_url)
    response.raise_for_status()
    data = response.json()
    print("API Response:", data)  
    if data and data['results']:
        result = data['results'][0]
        if 'properties' in result and 'thumbnail' in result['properties']:
            image_url = result['properties']['thumbnail']
            return image_url
    raise ValueError("No thumbnail link found for the given location.")
    
# dowload the data gotten from the api  

def download(lon,lat,file):
   try:
        image_url = getImage(lat, lon)
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        file_path = os.path.join('imgs', file)
        image.save(file_path)
        print(f"Downloaded : {file}")
   except Exception as e:
    print(f"Error: {e}")
   
download(longitude,latitude,filename)