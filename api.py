from nt import error
from urllib.error import URLError
import urllib.request
import json

api_post = "https://jsonplaceholder.typicode.com/posts/"


try:
    response = urllib.request.urlopen(api_post)

    data = response.read()
    json_data = json.loads(data.decode("utf-8"))
    print(json_data)
    response.close()

except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")
