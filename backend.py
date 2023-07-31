import requests

API_key="dc4d4364c3ecb10d994ba0ea93eca7d4"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data=data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind=="Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind=="sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo",forecast_days=3,kind="Temperature"))