# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

************* Module app
app.py:79:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:83:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:91:60: C0303: Trailing whitespace (trailing-whitespace)
app.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:122:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:35:4: W0702: No exception type(s) specified (bare-except)
app.py:44:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:56:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:73:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:105:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:138:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:153:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:160:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:172:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:2:0: C0411: standard import "secrets" should be placed before third party import "flask.Flask" (wrong-import-order)

************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)

************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:22:0: W0102: Dangerous default value [] as argument (dangerous-default-value)

************* Module init_db
init_db.py:14:0: C0304: Final newline missing (missing-final-newline)
init_db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
init_db.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
init_db.py:9:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

************* Module items
items.py:42:0: C0301: Line too long (105/100) (line-too-long)
items.py:51:0: C0301: Line too long (101/100) (line-too-long)
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:56:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)

************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 7.60/10

---

## Perustelut

### Docstring-ilmoitukset
Suurin osa raportin ilmoituksista liittyy puuttuviin docstring-kommentteihin moduuleissa ja funktioissa. Tietoisesti jätetty käyttämättä docstring-kommentteja.

### Trailing whitespace
Joissakin riveissä on ylimääräisiä välilyöntejä (esim. app.py:79, 83, 91, 93, 122). Nämä eivät estä sovelluksen toimintaa, mutta Pylint huomauttaa niistä.

### Import-ilmoitukset
Pylint saattaa antaa E0401-virheen, vaikka kirjastot (Flask, Werkzeug) ovat asennettu ympäristössä. Tämä ei haittaa sovelluksen toimintaa.

### Vaaralliset oletusarvot
Joissakin funktioissa (db.py) on käytetty tyhjää listaa oletusarvona. Sovellus ei kuitenkaan muokkaa kyseistä listaa, joten riskiä ei synny.

### Liian pitkät rivit
items.py:42 ja 51 sisältävät rivejä, jotka ovat yli 100 merkin pituisia. Koodi toimii, mutta Pylint antaa huomautuksen tyyliseikasta.

### Tarpeeton else / inconsistent return
Joissakin funktioissa käytetään else-haaraa, vaikka return olisi jo suoritettu, tai palautusarvot voivat olla epäjohdonmukaisia. Sovellus toimii silti.

### Vakion nimi
config.py: secret_key ei ole UPPER_CASE, mutta sovellus käyttää sitä oikein.

**Yhteenveto:** Sovellus toimii, vaikka Pylint antaa useita tyyli ja dokumentointihuomautuksia.  