# Kirja-arvostelut

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen arvosteluja. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään arvosteluita.
* Käyttäjä näkee sovellukseen lisätyt arvostelut. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.
* Käyttäjä pystyy etsimään arvosteluita hakusanalla. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä arvosteluita.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät arvostelut.
* Käyttäjä pystyy valitsemaan arvosteluille yhden tai useamman luokittelun (esim. genre, kieli, vuosi)
* Sovelluksen pääasiallinen tietokohde on kirja ja toissijainen tietokohde on kirjaan liittyvä kommentti ja arvostelu.

*  Kloonaa repository GitHubista:

git clone https://github.com/karitakk/kirja-arvostelut.git
cd kirja-arvostelut

Luo virtuaaliympäristö ja aktivoi se:
python3 -m venv venv
source venv/bin/activate

Asenna Flask:
pip install flask

Luo tietokanta ja taulut:
sqlite3 database.db "CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);"

sqlite3 database.db "CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    review TEXT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
);"

Käynnistä sovellus:
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

Avaa selain ja mene osoitteeseen http://127.0.0.1:5000

- Rekisteröidy uudella tunnuksella

- Kirjaudu sisään

- Lisää uusi kirja-arvostelu
