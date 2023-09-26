# Задание:

Необходимо написать небольшое приложение на django и django_rest_framework

Модели:

Category - категории объявлений, поля: name
City - город объявления, поля: name
Advert - объявление, поля: created (дата создания), title, description, city, category, views

Вью:

/api/advert-list/ - json список объявлений со всеми полями + название города + название категории /api/advert// - json
detail view одного объявления со всеми полями, просмотр данного вью увеличивает счётчик просмотров в объявлении

Завернуть проект в докер (в конфигурации для локальной разработки). БД - любая. Добавление данных через админку.

Стоит уделить внимание производительности вашего решения. Кэширование использовать не нужно, достаточно оптимизации
работы с базой данных.

# Инструкция по запуску:

Вы должны были установить и запустить Docker. Более подробная информация
здесь - [Instructions](https://docs.docker.com/).

#### 1. Склонируйте репозиторий.

```bash
git clone git@github.com:MrKalister/ad_board_test.git
```

#### 2. Создайте и активируйте виртуальную среду(при необходимости).

Команда для установки виртуальной среды на Mac или Linux:

```bash
python3 -m venv env
source env/bin/activate
```

Команда для Windows:

```bash
python -m venv venv
. venv/Scripts/activate
```

#### 3. Перейдите в каталог infra.

```bash
cd infra
```

#### 4. Скопируйте файл ".env-example" и заполните своими данными.

```bash
cp .env-example .env
```

#### 5. Запустите docker-compose.

```bash
docker-compose up -d
```

### В процессе выполнения будут произведены следующие действия:

* Тестирование;
* Создание и установка миграций;
* Создание суперпользователя;
* Загрузка fixtures

Это поведение можно изменить в docker-compose, убрав ненужные команды.

#### 6. Enjoy.

open [URL](http://127.0.0.1/recipes) and enjoy.
Документация API:
[Redoc](http://127.0.0.1:8000/redoc/)
[Swagger](http://127.0.0.1:8000/swagger/)

### Author

**Novikov Maxim** - [github](http://github.com/MrKalister)