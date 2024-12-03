### Analyse av bysykkeldata


Denne analysen tar for seg bydeler i Oslo og lokasjoner av bysykkelstasjoner. Dataene er hentet fra Oslo Bysykkel og bydeler med folketall.

#### Filer

pipeline.ipynb: Jupyter Notebook med kode for å hente og behandle dataene, viser også grafer generert med dataen.
api_exploration.ipynb: Jupyter Notebook med kode for å utforske Oslo Bysykkel API

Mappe OBA: Bruker writer framework for å lage interaktivt kart, som ved klikk på en bydel kan se plottene med informasjon om bydelen. Ble ikke ferdig med denne, så plottene vil ikke vises. Ble en del jobb med kovertering vekk ifra folium, og møtte på en del problemer med serialisation ettersom Writer ikke støtter geopandas sin geometry kolonne.

#### Sette opp

Python 3.12 eller nyere er anbefalt for å kjøre koden. Ettersom hint typing er brukt. Kjør 
```
pip install -r requirements.txt
```
for å installere nødvendige biblioteker

#### Kjøre

Kjøre igjennom alle cellene i pipeline.ipynb

#### NB
credentials.py er lastet opp for at det skal kjøres sømløst. Bare å sette inn egne API nøkler om ønskelig.

#### Teste ut OBA, (Oslo bysykkel analyse)

Laste ned writer
```
pip install writer
```
for så å navigere til mappen med oppgave.
Da kjøres 
```
writer run OBA
```
Når dette gjøres i terminal vil en link til lokalt hostet nettside vises:
App is available at: http://127.0.0.1:3005
som man kan åpne i nettleser.

