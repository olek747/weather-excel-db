from Services.OpenWeatherAPI import fetch_weather
from Services.excel_files import save_to_excel, read_excel_file
from Services.dashboard import create_plots
from config import Config
import time

while True:
    weather = fetch_weather()
    save_to_excel(weather)
    # weather_data = read_excel_file(Config.XLSX_PATH)
    weather_data = read_excel_file("./services/pogoda_rozszerzona.xlsx")
    create_plots(weather_data)
    print("Pobrałem dane")
    time.sleep(1000)