from data import nazwa, obiekty, pracownicy
from crud import read_festiwal, add_festiwal, search_festiwal, remove_festiwal, update_festiwal, read_workers, add_workers, search_workers, remove_workers, update_workers,read_miejsca,add_miejsca, search_miejsca, remove_miejsca, update_miejsca, full_map, full_map_1, full_map_pracownicy, show_pracownicy_festiwalu, show_miejsca_festiwalu

if __name__ == '__main__':
    print('Logowanie')

    Login = "programowanie"
    Haslo = "2024"
    login: str = input("Podaj login:")
    haslo: str = input("Podaj haslo:")
    if Login == login and Haslo == haslo:
        print("poprawne dane logowania")
    else:
        print("Błędny login lub hasło")
        login: str = input("Podaj login:")
        haslo: str = input("Podaj haslo:")

def main() -> None:
    while True:
        print('0. zakończ program ')
        print('1. wyświetl festiwale ')
        print('2. dodaj nowy festiwal')
        print('3. wyszukaj festiwal')
        print('4. usuń festiwal')
        print('5. zaaktualizuj festiwal')
        print('6. wyświetl zbiorową mapę festiwali')
        print('7. wyświetl obiekty')
        print('8. dodaj obiekty')
        print('9. wyszukaj obiekt')
        print('10. usuń obiekt')
        print('11. zaktualizuj obiekt')
        print('12. wyświetl zbiorową mapę obiektów')
        print('13. wyświetl pracowników')
        print('14. dodaj nowego pracownika')
        print('15. wyszukaj pracownika')
        print('16. usuń pracownika')
        print('17. edytuj pracownika')
        print('18. wyświetl mapę zbiorową pracowników')
        print('19. wyszukaj pracownika, który pracuje w danym festiwalu')
        print('20. wyszukaj lokalizację dla festiwalu')






        menu_option = input('wybierz opcje menu')
        if menu_option == "0": break
        if menu_option == "1": read_festiwal(nazwa)
        if menu_option == "2": add_festiwal(nazwa)
        if menu_option == "3": search_festiwal(nazwa)
        if menu_option == "4": remove_festiwal(nazwa)
        if menu_option == "5": update_festiwal(nazwa)
        if menu_option == "6": full_map(nazwa)
        if menu_option == "7": read_miejsca(obiekty)
        if menu_option == "8": add_miejsca(obiekty)
        if menu_option == "9": search_miejsca(obiekty)
        if menu_option == "10": remove_miejsca(obiekty)
        if menu_option == "11": update_miejsca(obiekty)
        if menu_option == "12": full_map_1(obiekty)
        if menu_option == "13": read_workers(pracownicy)
        if menu_option == "14": add_workers(pracownicy)
        if menu_option == "15": search_workers(pracownicy)
        if menu_option == "16": remove_workers(pracownicy)
        if menu_option == "17": update_workers(pracownicy)
        if menu_option == "18": full_map_pracownicy(pracownicy)
        if menu_option == "19": show_pracownicy_festiwalu(nazwa, pracownicy)
        if menu_option == "20": show_miejsca_festiwalu(nazwa, obiekty)




if __name__ == '__main__':
    main()


