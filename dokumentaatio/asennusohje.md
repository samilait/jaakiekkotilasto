# Asennusohje

## Paikallinen asennus

Kopioi sovelluksen tarvitsemat tiedostot git repositorysta painamalla "Clone or download" nappulaa.
Komentorivill� anna seuraava komento:

```
git@github.com:samilait/jaakiekkotilasto.git
```

K�ytt�m�ll� Visual Studio Codea ja siihen asennettua PlatformIO terminaalia k�ytt�m�ll� aktivoidaan virtuaaliymp�rist� seuraavalla komennolla:

```
venv\Scripts\activate.ps1
```

Sevelluksen vaatimat kirjastot ladataan komentorivill� seuraavasti:
```
pip install -r requirements.txt
```

Ja sovellus k�ynnistet��n komennolla
```
python run.py
```

Siirry selaimeen osoitteeseen: http://127.0.0.1:5000 (ilmoitetaan k�ynnistyksen yhteydess� logissa).
T�ss� vaiheessa tietokannan taulut ovat tyhji�. Niihin voidaan lis�t� sis�lt�� noudattamalla k�ytt�ohjeita.

Admin k�ytt�j�� ei my�sk��n kannassa ole valmniina, vaan se on luotava manuaalisesti. Avaa sqlite tietokanta komentorivill� seuraavasti:

```
cd application
sqlite3 icehockey.db
```
Seuraavaksi luo admin tunnukset:
```
INSERT INTO account (name, username, password) VALUES ('dallas stars','dallas', 'stars');
```

## Sovellus Herokuun

Komentorivill� annetaan seuraava komento

```
heroku create [k�ytt�j�n_valitsema_sovellusnimi]
```
Seuraavaksi lis�t��n paikalliseen versionhallintaan tieto Herokusta.

```
heroku remote add heroku
```

Sovellus l�hetet��n Herokuun komennolla:
```
git add .
git commit -m "initial commit"
git push heroku master
```

Lis�t��n seuraavaksi sovelluksen k�ytt��n tieto siit�, ett� sovellus on Herokussa ja luodaan lis�ksi tietokanta herokuun:

```
heroku config:set HEROKU=1
heroku addons:add heroku-postgresql:hobby-dev
```

Admin tunnukset on luotava viel� erikseen heroku tietokantaan. T�m� tapahtuu komentorivill� seuraavasti:

```
heroku pg:psql
INSERT INTO account (name, username, password) VALUES ('dallas stars','dallas', 'stars');
```
