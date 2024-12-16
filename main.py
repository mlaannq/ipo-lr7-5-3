import json
kolvo = 0
while True:
    print("\n выберите пункт из предложенного в меню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")

    choice = input("\nВыберите пункт из меню: 1,2,3,4 или 5 ")

    if choice == '1':
        with open('citi.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for city in data:
                print(f"\n№: {city['id']}")
                print(f"Название: {city['name']}")
                print(f"Страна: {city['country']}")
                print(f"Является ли большим(>100k): {city['is_big']}")
                print(f"Численность населения: {city['people_count']}")
        kolvo += 1

    elif choice == '2':
        # Вывод записи по id
        id_find = input("Введите id записи о городе, по которой хотите сделать вывод информации: \n")
        with open('citi.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            found = False
            for city in data:
                if city['id'] == id_find:
                    print(f"\n=============== Найдено ===============")
                    print(f"№: {city['id']}")
                    print(f"Название: {city['name']}")
                    print(f"Страна: {city['country']}")
                    print(f"Является ли большим(>100k): {city['is_big']}")
                    print(f"Численность населения: {city['people_count']}")
                    found = True
                    break
            if not found:
                print(f"\n=============== Не найдено ===============")
        kolvo += 1

    elif choice == '3':
        new_id = input("Введите номер записи: \n")
        new_name = input("Введите название города: \n")
        new_country = input("Введите страну города: \n")
        new_is_big = input("Введите является ли большим(>100k, введите 'True' или 'False'): \n").strip().lower() == "true"
        new_people_count = input("Введите численность населения города: \n")

        new_city = {
            "id": new_id,
            "name": new_name,
            "country": new_country,
            "is_big": new_is_big,
            "people_count": new_people_count
        }
        with open('citi.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(new_city)
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
        kolvo += 1

    elif choice == "4":
        find_to_delete = input("Введите номер записи, которую вы хотите удалить: ")
        with open('citi.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            found = False
            for city in data:
                if city['id'] == find_to_delete:
                    print(f"\n=============== Найдено ===============")
                    print(f"№: {city['id']}")
                    print(f"Название: {city['name']}")
                    print(f"Страна: {city['country']}")
                    print(f"Является ли большим(>100k): {city['is_big']}")
                    print(f"Численность населения: {city['people_count']}")
                    confirmation = input("Введите 'да', если хотите удалить данный город: ").strip().lower()
                    if confirmation in ["да"]:
                        data.remove(city)
                        found = True
                    else:
                        print("Запись не удалена.")
                        break
            if not found:
                print("\n=============== Не найдено ===============")
            else:
                file.seek(0)
                file.truncate()
                json.dump(data, file, ensure_ascii=False, indent=4)
        kolvo += 1

    elif choice == "5":
        print(f"\nВсего выполненных операций с записями: {kolvo}")
        break

    else:
        print("Ввод неверный.")