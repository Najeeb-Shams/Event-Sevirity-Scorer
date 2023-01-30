import requests

def check_endpoint(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successful connection to endpoint")
            return True
        else:
            print("Unsuccessful connection to endpoint")
            return False
    except requests.exceptions.RequestException as e:
        print(e)
        return False

# # Test the endpoint connection
check_endpoint("https://skynet.coypu.org/wikievents-20160101-20221130/")


