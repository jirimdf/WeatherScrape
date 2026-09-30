from bs4 import BeautifulSoup 
import requests
import schedule 
import time

print("__          __        _   _               ")
print("\ \        / /       | | | |              ")
print(" \ \  /\  / /__  __ _| |_| |__   ___ _ __ ")
print("  \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__|")
print("   \  /\  /  __/ (_| | |_| | | |  __/ |   ")
print("    \/  \/ \___|\__,_|\__|_| |_|\___|_|   ")
print("                      By MDF              ")


def get_weather():
    response = requests.get("https://pocasi.seznam.cz/ceske-budejovice")
    web = response.text

    soup = BeautifulSoup(web, "html.parser")
    print()
    print("Lokalita České Budějovice:\n")

    # Teplota
    temperature = soup.find(name="span", class_="d_cB")
    if temperature:
        temperature = temperature.text.strip()
        print(f"Teplota: {temperature}")
    else:
        print("Nepodařilo se najít teplotu.")

    # Rychlost větru
    wind_speed = soup.find_all(name="div", class_="d_cJ")[3]
    if wind_speed:
        wind_speed_text = wind_speed.text.strip().split()[0]
        print(f"Rychlost větru: {wind_speed_text} m/s")
    else:
        print("Nepodařilo se najít rychlost větru.")

    # Srážky
    precipitation = soup.find_all(name="div", class_="d_cJ")[5]
    if precipitation:
        precipitation_text = precipitation.text.strip().split()[0]
        print(f"Srážky: {precipitation_text} mm")
    else:
        print("Nepodařilo se najít srážky.")

    # Bio zátěž
    bio_load = soup.find_all(name="div", class_="d_cJ")[2]
    if bio_load:
        bio_load_text = bio_load.text.strip().split()[0]
        print(f"Bio zátěž: {bio_load_text}")
    else:
        print("Nepodařilo se najít bio zátěž.")

    # Tlak vzduchu
    air_pressure = soup.find_all(name="div", class_="d_cJ")[1]
    if air_pressure:
        air_pressure_text = air_pressure.text.strip().split()[0]
        print(f"Tlak vzduchu: {air_pressure_text} hPa")
    else:
        print("Nepodařilo se najít tlak.")



# Data počasí při spuštění
get_weather()

# Spuštění každých 5 minut
schedule.every(5).minutes.do(get_weather)

# Spuštění opakovaně, pro zrušení Ctrl + C
while True:
    schedule.run_pending()
    time.sleep(1)

    