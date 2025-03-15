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
            if not tasks:
                print("Nie ma żadnych zadań.")

            for index, task in enumerate(tasks):
                print(f"{index}. {task}")

            print(f"Twoja lista zadań {tasks}")

#Zrobić żeby wykrywało, że lista jest pusta, a pożniej zrobić zadnie z chata żeby móc usuwać zadania

        elif user_input == 3:
            print("Zamykam program...")
            break
        else:
            print("Nie ma takiego zadnia!")
    except ValueError:
        print("Podanaj cyfrę z instukcji, żeby wywołać kod!")