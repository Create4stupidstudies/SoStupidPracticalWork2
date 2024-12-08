from datetime import datetime, timedelta

# Данные пользователей и услуг
users = [
    {
        'username': 'u',
        'password': 'u',
        'role': 'user',
        'subscription_type': 'Premium',
        'history': [],
        'created_at': '2024-09-01',
        'total_spent': 0,  # Сумма потраченных средств
        'subscription_end_date': datetime.now() + timedelta(days=30),  # Дата окончания абонемента
        'coach': None,  # Тренер-наставник
        'age': None,  # Возраст
        'height': None,  # Рост
        'weight': None,  # Вес
        'gender': None,  # Пол
        'visited_services': {},  # Словарь для отслеживания посещаемых услуг
        'recent_actions': []  # Список для хранения последних действий
    },
    {
        'username': 'a',
        'password': 'a',
        'role': 'admin'
    },
]

services = [
    {'name': 'Персональная тренировка', 'price': 1500, 'duration': '1 час'},
    {'name': 'Групповая тренировка', 'price': 800, 'duration': '1.5 часа'},
    {'name': 'Абонемент на месяц', 'price': 5000, 'duration': '1 месяц'},
    {'name': 'Фитнес-тестирование', 'price': 2000, 'duration': '2 часа'},
    {'name': 'Силовая тренировка', 'price': 1200, 'duration': '1 час'},
    {'name': 'Кардиотренировка', 'price': 1000, 'duration': '1 час'},
    {'name': 'Пилатес', 'price': 900, 'duration': '1.5 часа'},
    {'name': 'Йога', 'price': 850, 'duration': '1.5 часа'},
    {'name': 'Занятие по танцам', 'price': 700, 'duration': '1 час'},
    {'name': 'Тренировка для беременных', 'price': 1100, 'duration': '1 час'},
    {'name': 'Тренировка для пожилых', 'price': 950, 'duration': '1 час'},
    {'name': 'Тренировка с элементами боевых искусств', 'price': 1300, 'duration': '1.5 часа'},
    {'name': 'Семейная тренировка', 'price': 1400, 'duration': '1.5 часа'},
    {'name': 'Тренировка на выносливость', 'price': 1200, 'duration': '1 час'},
    {'name': 'Тренировка на гибкость', 'price': 900, 'duration': '1 час'},
    {'name': 'Тренировка с гирями', 'price': 1300, 'duration': '1 час'},
    {'name': 'Спортивная гимнастика', 'price': 1100, 'duration': '1.5 часа'},
    {'name': 'Тренировка с фитнес-резинками', 'price': 800, 'duration': '1 час'},
    {'name': 'Тренировка на TRX', 'price': 1500, 'duration': '1 час'},
    {'name': 'Занятие по аквааэробике', 'price': 950, 'duration': '1.5 часа'},
]

# Список тренеров
coaches = [
    {'name': 'Тренер 1', 'specialization': 'Силовые тренировки'},
    {'name': 'Тренер 2', 'specialization': 'Кардиотренировки'},
    {'name': 'Тренер 3', 'specialization': 'Йога'},
    {'name': 'Тренер 4', 'specialization': 'Пилатес'},
]

def authenticate(username, password):
    """Проверка подлинности пользователя."""
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None

def display_services(services):
    """Отображение списка услуг."""
    for index, service in enumerate(services, start=1):
        print(f"{index}. {service['name']} - Цена: {service['price']} - Длительность: {service['duration']}")

def log_user_action(user, action):
    """Логирование действий пользователя."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user['recent_actions'].append(f"{timestamp}: {action}")
    # Ограничиваем количество записей до 5
    if len(user['recent_actions']) > 5:
        user['recent_actions'].pop(0)

def get_positive_integer(prompt):
    """Получение положительного целого числа от пользователя."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Ошибка: введите корректное целое число.")

def user_menu(user):
    """Меню для пользователей."""
    while True:
        print("\nДобро пожаловать в фитнес-клуб!")
        print("Выберите действие:")
        print("1. Просмотреть доступные услуги")
        print("2. Купить услугу")
        print("3. Посмотреть историю посещений")
        print("4. Фильтровать и сортировать услуги")
        print("5. Просмотреть сумму потраченных средств")
        print("6. Проверить оставшееся время абонемента")
        print("7. Выбрать тренера")
        print("8. Обновить профиль")
        print("9. Выйти")

        choice = input("Ваш выбор: ")
        if choice == '1':
            display_services(services)
        elif choice == '2':
            # Фильтрация и сортировка перед покупкой
            while True:
                print("\nДоступные услуги для покупки:")
                display_services(services)
                criterion = input("Хотите отсортировать услуги? (да/нет): ").lower()
                if criterion == 'да':
                    sort_criterion = input("Введите критерий для сортировки (цена/название/посещаемость): ").lower()
                    if sort_criterion == 'цена':
                        sorted_services = sorted(services, key=lambda x: x['price'])
                    elif sort_criterion == 'название':
                        sorted_services = sorted(services, key=lambda x: x['name'])
                    elif sort_criterion == 'посещаемость':
                        sorted_services = sorted(services, key=lambda x: user['visited_services'].get(x['name'], 0),
                                                 reverse=True)
                    else:
                        print("Некорректный критерий.")
                        continue
                else:
                    sorted_services = services

                display_services(sorted_services)
                service_number = get_positive_integer("Введите номер услуги для покупки: ") - 1
                if 0 <= service_number < len(sorted_services):
                    service = sorted_services[service_number]
                    user['history'].append(service['name'])
                    user['total_spent'] += service['price']  # Увеличиваем сумму потраченных средств
                    log_user_action(user, f"Куплена услуга '{service['name']}'")  # Логируем действие

                    # Обновление даты окончания абонемента, если куплен абонемент на месяц
                    if service['name'] == 'Абонемент на месяц':
                        user['subscription_end_date'] += timedelta(days=30)

                    # Увеличиваем счетчик посещений услуги
                    user['visited_services'][service['name']] = user['visited_services'].get(service['name'], 0) + 1
                    print(f"Услуга '{service['name']}' успешно куплена!")
                    break
                else:
                    print("Некорректный номер услуги.")
        elif choice == '3':
            print("История посещений:", user['history'])
        elif choice == '4':
            print("Фильтрация и сортировка услуг доступны при покупке услуги.")
        elif choice == '5':
            print(f"Вы потратили всего: {user['total_spent']} рублей.")
        elif choice == '6':
            remaining_days = (user['subscription_end_date'] - datetime.now()).days
            if remaining_days > 0:
                print(f"До окончания абонемента осталось: {remaining_days} дней.")
            else:
                print("Ваш абонемент истёк.")
        elif choice == '7':
            print("\nВыберите тренера:")
            for index, coach in enumerate(coaches, start=1):
                print(f"{index}. {coach['name']} - Специализация: {coach['specialization']}")
            coach_choice = get_positive_integer("Введите номер тренера: ") - 1
            if 0 <= coach_choice < len(coaches):
                user['coach'] = coaches[coach_choice]['name']
                log_user_action(user, f"Выбран тренер: {user['coach']}")  # Логируем действие
                print(f"Вы выбрали тренера: {user['coach']}")
                # Сбор характеристик
                user['age'] = get_positive_integer("Введите ваш возраст: ")
                user['height'] = float(input("Введите ваш рост (в см): "))
                user['weight'] = float(input("Введите ваш вес (в кг): "))
                user['gender'] = input("Введите ваш пол (мужской/женский): ")
                print("Ваши характеристики сохранены.")
            else:
                print("Некорректный выбор тренера.")
        elif choice == '8':
            print("Обновление профиля:")
            new_password = input("Введите новый пароль: ")
            user['password'] = new_password
            log_user_action(user, "Обновлён пароль")  # Логируем действие
            print("Пароль успешно обновлён.")
        elif choice == '9':
            print("Вы вышли из системы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

def admin_menu():
    """Меню администратора."""
    global services
    while True:
        print("\nДобро пожаловать в систему управления фитнес-клубом!")
        print("Выберите действие:")
        print("1. Добавить услугу")
        print("2. Удалить услугу")
        print("3. Редактировать услугу")
        print("4. Просмотреть услуги")
        print("5. Управление пользователями")
        print("6. Просмотреть пользователей")
        print("7. Просмотреть последние действия пользователя")
        print("8. Просмотреть статистику")
        print("9. Выйти")

        choice = input("Ваш выбор: ")
        if choice == '1':
            name = input("Введите название услуги: ")
            try:
                price = float(input("Введите цену услуги: "))
                duration = input("Введите длительность услуги: ")
                services.append({'name': name, 'price': price, 'duration': duration})
                print("Услуга добавлена!")
            except ValueError:
                print("Ошибка: цена должна быть числом.")
        elif choice == '2':
            name = input("Введите название услуги для удаления: ")
            initial_count = len(services)
            services = [service for service in services if service['name'] != name]
            if len(services) < initial_count:
                print("Услуга удалена!")
            else:
                print("Услуга не найдена.")
        elif choice == '3':
            name = input("Введите название услуги для редактирования: ")
            for service in services:
                if service['name'] == name:
                    try:
                        service['price'] = float(input("Введите новую цену: "))
                        service['duration'] = input("Введите новую длительность: ")
                        print("Услуга обновлена!")
                    except ValueError:
                        print("Ошибка: цена должна быть числом.")
                    break
            else:
                print("Услуга не найдена.")
        elif choice == '4':
            print("\nСписок услуг:")
            display_services(services)
        elif choice == '5':
            manage_users()
        elif choice == '6':
            view_users()
        elif choice == '7':
            username = input("Введите имя пользователя для просмотра действий: ")
            for user in users:
                if user['username'] == username:
                    print(f"\nПоследние действия пользователя '{username}':")
                    for action in user['recent_actions']:
                        print(action)
                    break
            else:
                print("Пользователь не найден.")
        elif choice == '8':
            print(f"Всего услуг: {len(services)}")
            user_count = len(users)
            print(f"Количество пользователей: {user_count}")
        elif choice == '9':
            print("Вы вышли из системы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

def manage_users():
    """Управление пользователями."""
    while True:
        print("\nУправление пользователями:")
        print("1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Вернуться в главное меню")

        choice = input("Ваш выбор: ")
        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            role = input("Введите роль (user/admin): ")
            users.append({
                'username': username,
                'password': password,
                'role': role,
                'total_spent': 0,
                'subscription_end_date': datetime.now() + timedelta(days=30),  # Начальный срок абонемента
                'coach': None,  # Тренер-наставник
                'age': None,  # Возраст
                'height': None,  # Рост
                'weight': None,  # Вес
                'gender': None,  # Пол
                'visited_services': {},  # Словарь для отслеживания посещаемых услуг
                'recent_actions': []  # Список для хранения последних действий
            })
            print(f"Пользователь '{username}' добавлен!")
        elif choice == '2':
            username = input("Введите имя пользователя для удаления: ")
            initial_count = len(users)
            users[:] = [user for user in users if user['username'] != username]
            if len(users) < initial_count:
                print(f"Пользователь '{username}' удалён!")
            else:
                print("Пользователь не найден.")
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

def view_users():
    """Просмотр списка пользователей."""
    print("\nСписок пользователей:")
    for user in users:
        print(f"Имя пользователя: {user['username']}, Роль: {user['role']}, "
              f"Тип подписки: {user.get('subscription_type', 'Нет')}, "
              f"Дата создания: {user.get('created_at', 'Нет')}, "
              f"Сумма потраченных средств: {user['total_spent']}, "
              f"Дата окончания абонемента: {user['subscription_end_date'].date()}, "
              f"Тренер: {user['coach']}, Возраст: {user['age']}, Рост: {user['height']}, "
              f"Вес: {user['weight']}, Пол: {user['gender']}")
    if not users:
        print("Пользователи не найдены.")

def main():
    """Главная функция для запуска программы."""
    print("Пожалуйста, авторизуйтесь.")
    username = input("Логин: ")
    password = input("Пароль: ")

    user = authenticate(username, password)
    if user:
        if user['role'] == 'admin':
            admin_menu()
        else:
            user_menu(user)
    else:
        print("Неверный логин или пароль.")

if __name__ == "__main__":
    main()
