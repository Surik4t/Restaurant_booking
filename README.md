# Restoraint Booking Pet Project
### API-сервис бронирования столиков в ресторане

REST API для бронирования столиков в ресторане. Сервис позволяет создавать, просматривать и удалять брони, а также управлять столиками и временными слотами.

### Стек:
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* Docker

###  Модели: 
#### Table – столик в ресторане:
* id: int
* name: str (например, "Table 1")
* seats: int (количество мест)
* location: str (например, "зал у окна", "терраса")

#### Reservation:
* id: int
* customer_name: str
* table_id: int (FK на Table)
* reservation_time: datetime
* duration_minutes: int

### Методы API: 
#### Столики:
* GET /tables/ — список всех столиков
* POST /tables/ — создать новый столик
* DELETE /tables/{id} — удалить столик

#### Брони:
* GET /reservations/ — список всех броней
* POST /reservations/ — создать новую бронь
* DELETE /reservations/{id} — удалить бронь

### Логика бронирования:
* Нельзя создать бронь, если в указанный временной слот столик уже занят (пересечение по времени и table_id).
* Бронь может длиться произвольное количество минут.
* Валидации должны обрабатываться на уровне API (например, конфликт брони должен выдавать ошибку с пояснением).

# Установка и запуск
> Для запуска потребуется Docker
* Клонируем проект и устанавливаем зависимости
```
git clone https://github.com/Surik4t/Restaurant_booking.git
cd /Restauraint_booking
pip install requirements.txt
```
* Запускаем БД и приложение
```
docker-compose up -d
uvicorn app.main:app
```
АПИ-эндпоинты буду доступны по ссылке: http://127.0.0.1:8000/docs#/
