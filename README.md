# TrafficMagnit Litestar microservice

Мета: винести частину API, що зараз реалізована в Django DRF (`admin_panel/api/offer_walls.py`), в окремий мікросервіс на Litestar з асинхронним доступом до БД, окремим Dockerfile і проксуванням через Nginx.

## Стек

- Python 3.12+
- [Litestar](https://docs.litestar.dev/latest/) — фреймворк
- SQLAlchemy (async) + aiosqlite (для локальної БД)
- pydantic-settings — для читання `.env`
- uvicorn / granian — як ASGI-сервер
- Docker, docker-compose
- Nginx як reverse proxy

> Примітка: у вимогах вказаний Granian. У Windows-середовищі можуть бути проблеми зі стартом Granian, тому для локального запуску використовується uvicorn. У Docker-оточенні можна замінити CMD на запуск Granian.

