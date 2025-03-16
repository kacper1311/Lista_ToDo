tasks = []

while True:
    print("1.Dodaj zadanie, 2.Usuń zadanie 3.Pokaż listę, 4. Wyjdź")
    try:
        user_input = int(input("Wpisz: "))

        if user_input == 1:
            user_task = input("Podaj treść zadania: ")
            task = tasks.append(user_task)
            print(f"Dodano zadanie. Twoja lista zadań {tasks}")
        elif user_input == 2:
            if not tasks:
                print("Nie ma żadnych zadań.")
            else:
                try:
                    for index, task in enumerate(tasks, start=1):
                        print(f"{index}. {task}")

                    delete_task = int(input("Podaj numer zadania do usunięcia: "))

                    if 0 < delete_task < len(tasks):
                        deleted_task = tasks.pop(delete_task - 1)
                        print(f"Usunięto zadanie: {deleted_task}")
                    else:
                        print("Nie ma takigo zadania! Podaj poprawny numer zadania") 
                except:
                    print("Musisz podać numer zadania z listy żeby je usunąć!")
        elif user_input == 3:
            if not tasks:
                print("Nie ma żadnych zadań.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif user_input == 4:
            print("Zamykam program...")
            break
        else:
            print("Nie ma takiego zadnia!")
    except ValueError:
        print("Podanaj cyfrę z instukcji, żeby wywołać kod!")