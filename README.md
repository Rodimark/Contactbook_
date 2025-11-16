# Névjegyzék Alkalmazás - EZEJTQ

## Hallgató

**Neptun kód:** EZEJTQ

## Feladat Leírása

Egy egyszerű, felhasználóbarát névjegyzék alkalmazás Python és Tkinter használatával. Az alkalmazás lehetővé teszi névjegyek hozzáadását, szerkesztését és törlését, valamint az adatok JSON formátumban történő tárolását.

## Funkciók

- **Névjegyek megjelenítése:** Áttekinthető táblázatos nézetben (TreeView) három oszloppal: Név, Telefonszám, Email cím
- **Új névjegy hozzáadása:** Egyszerű párbeszédablakokkal történő adatbevitel
- **Névjegy szerkesztése:** A kiválasztott személy adatainak módosítása
- **Meglévő névjegy törlése:** Megerősítéssel történő törlés
- **Automatikus mentés:** Az adatok automatikusan mentésre kerülnek JSON fájlba
- **Részletes nézet:** A kiválasztott személy adatainak megjelenítése a táblázat alatt

## Használat

1. **Személy hozzáadása:** Kattints az "Új személy hozzáadása" gombra, add meg a nevet, telefonszámot és email címet
2. **Szerkesztés:** Válassz ki egy személyt a táblázatból, majd kattints a "Meglévő személy szerkesztése" gombra
3. **Törlés:** Válassz ki egy személyt, majd kattints a "Meglévő személy törlése" gombra és erősítsd meg a műveletet

## Osztályok

### ContactBook

A fő alkalmazás osztály, amely a névjegyzék funkcionalitását valósítja meg.

#### Attribútumok:
- `root`: A Tkinter főablak
- `contacts`: Dictionary, amely a névjegyeket tárolja (kulcs: név, érték: dictionary telefonszámmal és email címmel)
- `file_path`: A JSON fájl elérési útja (`nevjegyzek.json`)
- `treeview`: TreeView widget a névjegyek megjelenítéséhez
- `detail_label`: Label widget a kiválasztott névjegy részleteinek megjelenítéséhez
- `add_btn`, `edit_btn`, `delete_btn`: Gombok a műveletek végrehajtásához

#### Metódusok:

- `__init__(self, root)`: Az alkalmazás inicializálása, GUI elemek létrehozása
- `load_contacts(self)`: Névjegyek betöltése JSON fájlból
- `save_contacts(self)`: Névjegyek mentése JSON fájlba
- `refresh_list(self)`: A TreeView frissítése az aktuális névjegyekkel
- `show_contact_details(self, event)`: A kiválasztott névjegy részleteinek megjelenítése
- `add_contact(self)`: Új névjegy hozzáadása
- `edit_contact(self)`: Meglévő névjegy szerke
