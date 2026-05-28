from sqlmodel import create_engine, SQLModel, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# The engine handles the actual communication with the database file
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# Create the database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# This is our Dependency! It opens a session and closes it when done.
def get_session():
    with Session(engine) as session:
        yield session