class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []
    
    # Створюємо копію списку викладачів, щоб не змінювати оригінал
    available_teachers = list(teachers)

    while remaining_subjects:
        best_teacher = None
        best_cover = set()

        for teacher in available_teachers:
            # Знаходимо перетин предметів викладача та тих, що залишилися
            current_cover = teacher.can_teach_subjects.intersection(remaining_subjects)
            
            if not current_cover:
                continue
            
            # Жадібний вибір: більше предметів або менший вік
            if (best_teacher is None or 
                len(current_cover) > len(best_cover) or 
                (len(current_cover) == len(best_cover) and teacher.age < best_teacher.age)):
                
                best_teacher = teacher
                best_cover = current_cover

        # Якщо не знайшли викладача, який може викласти хоча б один залишковий предмет
        if best_teacher is None:
            return None

        # Призначаємо предмети та оновлюємо стан
        best_teacher.assigned_subjects = best_cover
        schedule.append(best_teacher)
        remaining_subjects -= best_cover
        available_teachers.remove(best_teacher)

    return schedule

if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")