# WeatherScrape

Konzolová aplikace v Pythonu, která stahuje aktuální počasí pro České Budějovice z webu [pocasi.seznam.cz](https://pocasi.seznam.cz/ceske-budejovice) a každých 5 minut ho automaticky aktualizuje.

> Výukový projekt zaměřený na web scraping a plánování opakovaných úloh.

## Funkce

- Zobrazení aktuálních údajů o počasí:
  - teplota
  - rychlost větru (m/s)
  - srážky (mm)
  - biozátěž
  - tlak vzduchu (hPa)
- Automatická aktualizace každých 5 minut (interval lze změnit)
- Ošetření chybějících dat – pokud se údaj nepodaří načíst, program vypíše hlášku a pokračuje

## Použité technologie

| Knihovna | Účel |
|---|---|
| [requests](https://pypi.org/project/requests/) | stažení HTML stránky |
| [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) | parsování HTML a vyhledání údajů |
| [schedule](https://pypi.org/project/schedule/) | plánování opakovaného spuštění |
| time (standardní knihovna) | čekací smyčka |

## Instalace

Požadavky: **Python 3.8+**

```bash
git clone https://github.com/jirimdf/WeatherScrape.git
cd WeatherScrape
pip install requests beautifulsoup4 schedule
```

Na Linuxu (Debian/Ubuntu) případně nejdřív doinstalujte pip:

```bash
sudo apt update
sudo apt install python3-pip
```

## Spuštění

```bash
python main.py
```

Program po spuštění ihned vypíše aktuální počasí a poté ho obnovuje každých 5 minut. Ukončení: **Ctrl + C**.

Ukázka výstupu:

```
Lokalita České Budějovice:

Teplota: 14°C
Rychlost větru: 3 m/s
Srážky: 0 mm
Bio zátěž: Nízká
Tlak vzduchu: 1024 hPa
```

## Jak to funguje

1. `requests` stáhne HTML stránku s počasím.
2. `BeautifulSoup` v ní najde jednotlivé údaje podle jejich popisků na stránce (např. „Tlak“, „Srážky“).
3. Funkce `get_weather()` údaje vypíše do konzole.
4. `schedule` spouští `get_weather()` každých 5 minut v nekonečné smyčce.

## Úpravy

- **Interval aktualizace** – v `main.py` změňte číslo v `schedule.every(5).minutes`.
- **Jiné město** – změňte URL v `requests.get(...)`, např. na `https://pocasi.seznam.cz/praha`.

## Známá omezení

Scraper je závislý na HTML struktuře webu pocasi.seznam.cz. Údaje hledá podle textových popisků, ne podle generovaných CSS tříd, takže běžné změny vzhledu přežije. Pokud web změní popisky nebo strukturu stránky, je potřeba kód upravit.

## Licence

Projekt je pod licencí [MIT](LICENSE).
