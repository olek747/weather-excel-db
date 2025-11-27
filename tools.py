from Services.OpenWeatherAPI import fetch_weather
from Services.excel_files import save_to_excel, read_excel_file
from config import Config
import time

def convert_to_celsius(temp_k):
    return round(temp_k - 273.15, 2)

def ms_to_kmh(speed_ms):
    return speed_ms * 3.6

while True:
    weather = fetch_weather()
    save_to_excel(weather)
    weather_data = read_excel_file(Config.XLSX_PATH)
    print("Pobrałem dane")
    time.sleep(10)