from sqlalchemy import BOOLEAN, INTEGER, VARCHAR, VARCHAR, Integer, MetaData, Table, Column


_all_ = 'user_table'
db_metadata = MetaData()

user_table = Table(
    'users',
    db_metadata,
    Column('id', INTEGER, primary_key=True),
    Column('username', VARCHAR(100), nullable=False),
    Column('email', VARCHAR(100), nullable=False, unique=True),
    Column('age', INTEGER, nullable=True),
    Column('is_active', BOOLEAN, nullable=False, default=True)
)