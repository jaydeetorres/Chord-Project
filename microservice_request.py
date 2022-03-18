# used to access random number from teammates microservice
import requests

def rng(limit = None):
    if limit is None:
        URL = "http://localhost:8080/random"
    else:
        URL = "http://localhost:8080/random/" + str(limit)

    r = requests.get(url = URL)
    
    data = r.json()

    rng = data["random"]
    return rng

if __name__ == "__main__":
    print(rng(100))
    print(rng())