from database import engine
from weather import Base


def init_db():
    print("Creating table...")
    Base.metadata.create_all(bind=engine)
    print("Successfully created.")


if __name__ == "__main__":
    init_db()
