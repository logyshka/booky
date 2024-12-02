import os
import random

import django
from faker import Faker

from core.models import Book, Author, Genre  # Замените 'myapp' на имя вашего приложения

# Настройка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booky.settings')  # Замените 'myproject' на имя вашего проекта
django.setup()

# Инициализация Faker
fake = Faker(locale='ru')


def create_authors(count: int = 10):
    authors = []
    for _ in range(count):
        author = Author.objects.create(
            fullname=fake.name_male()
        )
        authors.append(author)
    return authors


def create_books(count: int = 50, authors: list[Author] = None, genres: list[Genre] = None):
    """Создать случайные книги."""
    _authors = list(Author.objects.all())
    authors = _authors if authors is None else authors + _authors

    if genres is None:
        genres = list(Genre.objects.all())

    for _ in range(count):
        book = Book.objects.create(
            title=fake.sentence(nb_words=4),
            description=fake.text(max_nb_chars=1000),
            author=random.choice(authors),

        )
        # Добавляем случайные жанры
        book.genres.set(random.sample(genres, k=random.randint(1, min(3, len(genres)))))


def populate_database():
    """Заполнить базу данных случайными данными."""
    print("Создаем авторов...")
    authors = create_authors(10)
    print("Создаем книги...")
    create_books(100, authors=authors)
    print("Готово!")


if __name__ == '__main__':
    populate_database()
