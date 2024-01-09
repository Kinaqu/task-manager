tasks = {}  # Словарь для хранения задач

def add_task():
    task_id = len(tasks) + 1
    description = input("Введите описание задачи: ")
    tasks[task_id] = description
    print(f"Задача с ID {task_id} добавлена.")

def delete_task():
    task_id = int(input("Введите ID задачи для удаления: "))
    if task_id in tasks:
        del tasks[task_id]
        print(f"Задача с ID {task_id} удалена.")
    else:
        print("Задача с таким ID не найдена.")

def view_tasks():
    if not tasks:
        print("Список задач пуст.")
        return
    print("Список задач:")
    for task_id, description in tasks.items():
        print(f"ID: {task_id}, Описание: {description}")

def main():
    while True:
        print("\nМенеджер задач")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Просмотреть задачи")
        print("4. Выйти")
        
        choice = input("Выберите действие (1/2/3/4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()