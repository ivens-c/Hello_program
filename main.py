import random

# Список веселых комментариев
comments = [
    "Привет, звезда! Как прошел день?",
    "Приветствую, человек с лучшей улыбкой в мире!",
    "Привет, мастер веселья! Что нового?",
    "Здравствуй, источник позитивной энергии!",
    "Привет, гуру веселья! Как настроение?",
]

name = input("Привет! Как тебя зовут? ")
comment = random.choice(comments)
print(f"{comment} {name}!")

response = input("Хочешь услышать еще один веселый комментарий? (Да/Нет) ")
while response.lower() == "да":
    comment = random.choice(comments)
    print(f"{comment} {name}!")
    response = input("Хочешь услышать еще один веселый комментарий? (Да/Нет) ")

print("Спасибо за игру! Удачного дня!")
