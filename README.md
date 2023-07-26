# Asynchrone I/O-bewerkingen in Python

In deze repository vind je de in c’t magazine besproken Python-code: [1.py](artikel/1.py), [2.py](artikel/2.py), [3.py](artikel/3.py) en [4.py](artikel/4.py) geven de voortgang bij de ontwikkeling weer, [nanodirb.py](artikel/nanodirb.py) is de in het magazine beschreven rudimentaire Dirb-kloon en [dirb.py](dirb.py) de asynchroon werkende voltooide implementatie  (niet 1:1) van het origineel [Dirb](https://manpages.debian.org/bullseye/dirb/dirb.1.en.html).

## Voorbereiding

```bash
git clone https://github.com/cttester/asyncio.git
cd asyncio
pipenv install
```

## Gebruik

Bijvoorbeeld:

```
pipenv run ./dirb.py "http://example.com" \
  -w path-list1.txt -w path-list2.txt \
  -n 10
  -f \
  --csv \
  -o scan-result.csv
```

Waarbij `http://example.com` de basis-URL is van het te scannen domein. De paden in de met `-w` aangegeven bestanden (een pad per regel) worden bij het scannen aan de basis-URL toegevoegd.

De switch `-n` geeft aan, hoeveel workers parallel moeten werken, oftewel hoeveel scanacties er tegelijkertijd verwerkt zullen worden (standaard: 10).

Met de switch `--csv` produceert het script een uitvoer in CSV-formaat, die je bijvoorbeeld kunt openen in een spreadsheetprogramma.

Voor veel URL's geven webservers een redirect terug (HTTP-Status-Code 301 of 302). Zonder de switch `-f` registreert het script alleen de redirect, met deze switch volgt het script de URL waar de redirect heen leidt.

Standaard worden de resultaten op het scherm getoond. De switch `-o` voert ze naar een bestand uit.

Voer `dirb.py -h` in om ale mogelijke opdrachtopties te zien.


## Licentie

Zie [LICENSE](LICENSE)


## Copyright

Copyright ©️ 2023 [Oliver Lau](mailto:ola@ct.de), [Heise Medien GmbH & Co. KG](https://www.heise-gruppe.de/artikel/Heise-Medien-3904998.html)


## Aanwijzingen voor het gebruik

Deze software is geschreven voor leer- en voorbeelddoeleinden en niet voor productief gebruik. F&L Media, Heise Medien en de auteur zijn niet verantwoordelijk voor schade die ontstaat door het gebruik van deze software en geven geen garanties voor de volledigheid, juiste werking of geschiktheid voor gebruik.
