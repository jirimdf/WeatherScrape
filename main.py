from bs4 import BeautifulSoup 
import requests
import schedule 
import time

print("__          __        _   _               ")
print(r"\ \        / /       | | | |              ")
print(r" \ \  /\  / /__  __ _| |_| |__   ___ _ __ ")
print(r"  \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__|")
print(r"   \  /\  /  __/ (_| | |_| | | |  __/ |   ")
print(r"    \/  \/ \___|\__,_|\__|_| |_|\___|_|   ")
print("                      By MDF              ")


def get_value(soup, label):
    # Najde hodnotu podle popisku (např. "Tlak"), nezávisle na CSS třídách
    label_div = soup.find(name="div", string=label)
    if label_div:
        value_div = label_div.find_next_sibling(name="div")
        if value_div:
            return value_div.get_text(" ", strip=True)
    return None


def get_weather():
    response = requests.get("https://pocasi.seznam.cz/ceske-budejovice", timeout=10)
    web = response.text

    soup = BeautifulSoup(web, "html.parser")
    print()
    print("Lokalita České Budějovice:\n")

    # Teplota
    municipality = soup.find(attrs={"data-e2e": "mol-map-municipality"})
    temperature = municipality.find_next(name="span") if municipality else None
    if temperature:
        temperature = temperature.get_text(strip=True)
        print(f"Teplota: {temperature}")
    else:
        print("Nepodařilo se najít teplotu.")

    # Rychlost větru
    wind_speed = get_value(soup, "Rychlost")
    if wind_speed:
        print(f"Rychlost větru: {wind_speed}")
    else:
        print("Nepodařilo se najít rychlost větru.")

    # Srážky
    precipitation = get_value(soup, "Srážky")
    if precipitation:
        print(f"Srážky: {precipitation}")
    else:
        print("Nepodařilo se najít srážky.")

    # Bio zátěž
    bio_load = get_value(soup, "BIO")
    if bio_load:
        print(f"Bio zátěž: {bio_load}")
    else:
        print("Nepodařilo se najít bio zátěž.")

    # Tlak vzduchu
    air_pressure = get_value(soup, "Tlak")
    if air_pressure:
        print(f"Tlak vzduchu: {air_pressure}")
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

    