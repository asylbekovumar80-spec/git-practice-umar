# 1. Выведите сегодняшнюю дату в формате ДД.ММ.ГГГГ.
#
# 2. Выведите текущее время в формате ЧЧ:ММ.
#
# 3. Создайте дату экзамена 20 декабря 2026 года и выведите её.
#
# 4. Преобразуйте строку "08.03.2027" в объект datetime.
#
# 5. Выведите дату, которая наступит через 30 дней.
#
# 6. Пользователь вводит дату ДД.ММ.ГГГГ. Посчитайте, сколько дней
#    прошло с этой даты. Отдельно обработайте дату из будущего.
#
# 7. Пользователь вводит дедлайн. Выведите:
#    - "Дедлайн сегодня";
#    - "До дедлайна осталось N дней";
#    - "Дедлайн просрочен на N дней".
#

from datetime import datetime, timedelta
now = datetime.now()
today = now.date()
print("1. Бүгүнкү дата: ДД.ММ.ГГГГ.:", today.strftime("%d.%m.%Y"))
print("2. Учурдагы убакыт:ЧЧ:ММ: ", now.strftime("%H:%M"))
exam_date = datetime(2026, 12, 20).date()
print("3. Экзамен күнү:", exam_date.strftime("%d.%m.%Y"))
date_str = "08.03.2027"
parsed_date = datetime.strptime(date_str, "%d.%m.%Y")
print("4. datetime объектиси:", parsed_date)
future_date = today + timedelta(days=30)
print("5. 30 күндөн кийинки дата:", future_date.strftime("%d.%m.%Y"))

print("-" * 30)

user_input1 = input("Дата киргизиңиз (ДД.ММ.ГГГГ): ")
user_date = datetime.strptime(user_input1, "%d.%m.%Y").date()

if user_date < today:
    days_passed = (today - user_date).days
    print("Бул датадан бери өткөн күндөр:", days_passed)
elif user_date > today:
    days_future = (user_date - today).days
    print("Бул келечектеги дата. Ага чейин калган күндөр:", days_future)
else:
    print("Бул бүгүнкү күн.")

print("-" * 30)

user_input2 = input("Дедлайнды киргизиңиз (ДД.ММ.ГГГГ): ")
deadline = datetime.strptime(user_input2, "%d.%m.%Y").date()

if deadline == today:
    print("Дедлайн бүгүн")
elif deadline > today:
    days_left = (deadline - today).days
    print("Дедлайнга чейин калды:", days_left, "күн")
else:
    days_overdue = (today - deadline).days
    print("Дедлайн өтүп кетти:", days_overdue, "күн")
