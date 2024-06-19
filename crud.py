import folium
import requests

from bs4 import BeautifulSoup



def read_festiwal(nazwa: list) -> None:
    print("Wyświetl listę festiwali: ")
    for festiwal in nazwa:
        print(f" Festiwal {festiwal['name']} odbywa się w: {festiwal['location']} ")

def add_festiwal(festiwale: list) -> None:
    print("Dodaj nowy festiwal:")
    new_festiwal: dict = {
        'name': input('Wpisz nazwę nowego festiwalu: '),
        'location': input('Wpisz lokalizację nowego festiwalu: '),
    }
    festiwale.append(new_festiwal)

def search_festiwal(nazwa: list) -> dict:
    name: str = input("Który festiwal chcesz wyszukać: ")
    for festiwal in nazwa:
        if festiwal["name"] == name:
            print(festiwal)
            return festiwal

def remove_festiwal(nazwa: list) -> None:
    name: str = input("Który festiwal chcesz usunąć? ")
    for festiwal in nazwa:
        if festiwal["name"] == name:
            nazwa.remove(festiwal)

def update_festiwal(nazwa: list) -> None:
    name: str = input("Który festiwal chcesz zmienić? ")
    for festiwal in nazwa:
        if festiwal["name"] == name:
            festiwal['name'] = input("Wpisz nową nazwę: ")
            festiwal['location'] = input("Wpisz nową lokalizację: ")


# funkcje dla obiektow
def read_miejsca(obiekty: list) -> None:
    print("Wyświetl listę obiektów: ")
    for miejsca in obiekty:
        print(f" {miejsca['name']} znajduje się w: {miejsca['location']} ")

def add_miejsca(obiekty: list) -> None:
    print("Dodaj nowe miejsce:")
    new_miejsce: dict = {
        'name': input('Wpisz nazwę nowego obiektu: '),
        'location': input('Wpisz lokalizację nowego obiektu: '),
    }
    obiekty.append(new_miejsce)


def search_miejsca(obiekty: list) -> dict:
    name: str = input("Który obiekt chcesz wyszukać: ")
    for miejsca in obiekty:
        if miejsca["name"] == name:
            print(miejsca)
            return miejsca

def remove_miejsca(obiekty: list) -> None:
    name: str = input("Który obiekty chcesz usunąć? ")
    for miejsca in obiekty:
        if miejsca["name"] == name:
            obiekty.remove(miejsca)

def update_miejsca(obiekty: list) -> None:
    name: str = input("Który obiekt chcesz zmienić? ")
    for miejsca in obiekty:
        if miejsca["name"] == name:
            miejsca["name"] = input("Wpisz nową nazwę obiektu: ")
            miejsca["location"] = input("Wpisz nową lokalizację obiektu: ")

#funkcje dla pracownicy

def read_workers(pracownicy: list) -> None:
    print("Wyświetl listę pracowników: ")
    for workers in pracownicy:
        print(f" Pracownik: {workers['name']} {workers['surname']}, pracuje w : {workers['location']} ")

def add_workers(employes: list) -> None:
    print("Dodaj nowego pracownika:")
    new_workers: dict = {
        'name': input('Wpisz imię nowego pracownika: '),
        'surname': input('Wpisz nazwisko nowego pracownika: '),
        'location': input('Wpisz lokalizację nowego pracownika: '),
    }
    employes.append(new_workers)

def search_workers(pracownicy: list) -> dict:
    name: str = input("Którego pracownika chcesz wyszukać: ")
    for workers in pracownicy:
        if workers["name"] == name:
            print(workers)
            return workers

def remove_workers(pracownicy: list) -> None:
    name: str = input("Którego pracownika chcesz usunąć? ")
    for workers in pracownicy:
        if workers["name"] == name:
            pracownicy.remove(workers)

def update_workers(pracownicy: list) -> None:
    name: str = input("Którego pracownika chcesz edytować? ")
    for workers in pracownicy:
        if workers["name"] == name:
            workers["name"] = input("Wpisz nowe imię: ")
            workers['surname'] = input('Wpisz nowe nazwisko:')
            workers["location"] = input("Wpisz nową lokalizację: ")

#mapy

def full_map(users):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for user in users:
        url = (f"https://pl.wikipedia.org/wiki/{user['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{user['name']},\n{user['location']}",
                      icon=folium.Icon(color='black')).add_to(map)

    map.save(f'map.html')

def full_map_1(obiekty):
    map_obiekty = folium.Map(location=[52, 20], zoom_start=6)
    for miejsca in obiekty:
        url = (f"https://pl.wikipedia.org/wiki/{miejsca['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{miejsca['name']},\n{miejsca['location']}",
                      icon=folium.Icon(color='green')).add_to(map_obiekty)
    map_obiekty.save(f'map_obiekty.html')


def full_map_pracownicy(pracownicy):
    map_pracownicy = folium.Map(location=[52, 20], zoom_start=6)
    for workers in pracownicy:
        url = (f"https://pl.wikipedia.org/wiki/{workers['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{workers['name']} {workers['surname']},\n{workers['location']}",
                      icon=folium.Icon(color='red')).add_to(map_pracownicy)
    map_pracownicy.save(f'map_pracownicy.html')


