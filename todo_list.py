tasks = []

while True:
    print("1.Dodaj zadanie, 2.Pokaż listę, 3. Wyjdź")
    try:
        user_input = int(input("Wpisz: "))

        if user_input == 1:
            user_task = input("Podaj treść zadania: ")
            task = tasks.append(user_task)
            print(f"Dodano zadanie. Twoja lista zadań {tasks}")
        elif user_input == 2:
            print(f"Twoja lista zadań {tasks}")
        elif user_input == 3:
            break
        else:
            print("Nie ma takiego zadnia!")
    except ValueError:
        print("Podanaj cyfrę z instukcji, żeby wywołać kod!")