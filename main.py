import file_operations
from faker import Faker
from random import randint, choice, sample


print(file_operations.VERSION)

fake = Faker("ru_RU")

skills_list = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]
skills = sample(skills_list, 3)

context = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "job": fake.job(),
    "town": fake.city(),
    "strength": randint(3, 18),
    "agility": randint(3, 18),
    "endurance": randint(3, 18),
    "intelligence": randint(3, 18),
    "luck": randint(3, 18),
    "skill_1": skills[0],
    "skill_2": skills[1],
    "skill_3": skills[2],
}

file_operations.render_template("charsheet.svg", "charsheet_test.svg", context)
