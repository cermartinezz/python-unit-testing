import requests


def get_location(ip):
    url = f"http://freeipapi.com/api/json/{ip}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    return {
        "country": data["countryName"],
        "city": data["cityName"],
        "region": data["regionName"],
    }


if __name__ == "__main__":
    print(get_location("8.8.8.8"))
