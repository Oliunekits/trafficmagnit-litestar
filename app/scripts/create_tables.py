from sqlalchemy import create_engine
from app.config import settings
from app.models import Base
import os


def main() -> None:
    db_url = settings.database_url

    if db_url.startswith("sqlite+aiosqlite:///"):
        db_url = db_url.replace("sqlite+aiosqlite:///", "sqlite:///")
    elif db_url.startswith("sqlite+aiosqlite://"):
        db_url = db_url.replace("sqlite+aiosqlite://", "sqlite:///")

    engine = create_engine(db_url)

    if db_url.startswith("sqlite:///"):
        db_path = db_url.replace("sqlite:///", "")
        print("Creating tables in:", os.path.abspath(db_path))

    Base.metadata.create_all(bind=engine)
    print("Таблиці створено!")


if __name__ == "__main__":
    main()
