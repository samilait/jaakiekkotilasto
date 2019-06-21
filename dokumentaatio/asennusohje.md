# Asennusohje

## Paikallinen asennus

Kopioi sovelluksen tarvitsemat tiedostot git repositorysta painamalla "Clone or download" nappulaa.
Komentorivillä anna seuraava komento:

```
git@github.com:samilait/jaakiekkotilasto.git
```

Käyttämällä Visual Studio Codea ja siihen asennettua PlatformIO terminaalia käyttämällä aktivoidaan virtuaaliympäristö seuraavalla komennolla:

```
venv\Scripts\activate.ps1
```

Sevelluksen vaatimat kirjastot ladataan komentorivillä seuraavasti:
```
pip install -r requirements.txt
```

Ja sovellus käynnistetään komennolla
```
python run.py
```

Siirry selaimeen osoitteeseen: http://127.0.0.1:5000 (ilmoitetaan käynnistyksen yhteydessä logissa).
Tässä vaiheessa tietokannan taulut ovat tyhjiä. Niihin voidaan lisätä sisältöä noudattamalla käyttöohjeita.

Admin käyttäjää ei myöskään kannassa ole valmniina, vaan se on luotava manuaalisesti. Avaa sqlite tietokanta komentorivillä seuraavasti:

```
cd application
sqlite3 icehockey.db
```
Seuraavaksi luo admin tunnukset:
```
INSERT INTO account (name, username, password) VALUES ('dallas stars','dallas', 'stars');
```

## Sovellus Herokuun

Komentorivillä annetaan seuraava komento

```
heroku create [käyttäjän_valitsema_sovellusnimi]
```
Seuraavaksi lisätään paikalliseen versionhallintaan tieto Herokusta.

```
heroku remote add heroku
```

Sovellus lähetetään Herokuun komennolla:
```
git add .
git commit -m "initial commit"
git push heroku master
```

Lisätään seuraavaksi sovelluksen käyttöön tieto siitä, että sovellus on Herokussa ja luodaan lisäksi tietokanta herokuun:

```
heroku config:set HEROKU=1
heroku addons:add heroku-postgresql:hobby-dev
```

Admin tunnukset on luotava vielä erikseen heroku tietokantaan. Tämä tapahtuu komentorivillä seuraavasti:

```
heroku pg:psql
INSERT INTO account (name, username, password) VALUES ('dallas stars','dallas', 'stars');
```
