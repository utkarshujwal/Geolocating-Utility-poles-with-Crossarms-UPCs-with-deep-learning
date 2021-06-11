# required Libraries 
import google_streetview.api
import google_streetview.helpers


lat = 42.0451
lon = -87.6051

radius = 1 
increment = 0.2

download_data_dir = "./GSV_images/"

api_key = ""

"""
SIZE : 
    Adjust size of the images up to 640 by 640 pixels with the --size argument and providing <width>x<height> values 
    (the default is 640x640).

HEADING : 
    Adjust the heading of the camera with the --heading argument, 
    where 0 and 360 are north, 90 is east, 180 is south, and 270 is west.

FOV : 
    Adjust the image’s horizontal field of view with the --fov argument, 
    which represents zoom values of up to 120 (the default is 90).

PITCH : 
    Adjust the camera’s up and down angle with the --pitch argument, 
    where positive values up to 90 degrees indicate straight up and negative values down to -90 indicate straight down.
    (the default is 0). 

"""


params = {
        'size': '640x640',   # the size of the image to be scraped. 
        'heading': '0;90;180;270', # the 
        'fov': '90;120',
        'pitch': '0',
        }


def get_images(lattitude, longitude, radius, increment, api_key, data_dir, parameters):
    lat_difference = increment/69
    long_difference = increment/54

    lat_dim = radius/(69*2)
    long_dim = radius/(54*2)

    # making a list of all the latitude and longitude intersections 

    lat_lower = lattitude - lat_dim
    long_east = longitude + long_dim

    lat_upper = lattitude + lat_dim
    long_west = longitude - long_dim

    cordinates = []

    lat = lat_lower
    lon = long_west

    while lat <=lat_upper:
        while lon <= long_east:
            temp = str(lat) +','+str(lon)+';'
            cordinates.append(temp)
            lon += long_difference
        lat += lat_difference
        lon = long_west

            
    API_locations = ''.join(cordinates)

    apiargs = parameters 

    apiargs['location'] = API_locations
    apiargs['key'] = api_key


    # Get a list of all possible queries from multiple parameters
    api_list = google_streetview.helpers.api_list(apiargs)

    print( 'api_list done!')

    # Create a results object for all possible queries provides metadata 
    # of downloaded images
    results = google_streetview.api.results(api_list)

    print("downloading starting")

    #Download images to directory 'downloads'
    results.download_links(data_dir)

    print("downloading done !")


get_images(lat, lon, radius, increment, api_key, download_data_dir,params)
