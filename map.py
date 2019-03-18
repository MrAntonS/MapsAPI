import requests


geocoder_api_server = "http://static-maps.yandex.ru/1.x/"
def get_map(x, y, zoom, filename, map_type="sat"):
    params = {"l": map_type,
              "z": str(zoom),
              "ll": ",".join([str(x),str(y)])}
    response = requests.get(geocoder_api_server, params=params)
    if not response:
        err = "Http статус:"+str(response.status_code)+"("+str(response.reason)+")"
        return False, err
    
    try:
        with open(filename, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        return False, ex
    return True, None


if __name__ == "__main__":
    x, y = '37', '55'
    zoom = 10
    filename = "map.png"
    print(get_map(x, y, zoom, filename, "map") )