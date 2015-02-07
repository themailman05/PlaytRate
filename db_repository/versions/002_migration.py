from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
twitter_ball = Table('twitter_ball', pre_meta,
    Column('name', VARCHAR(length=100), primary_key=True, nullable=False),
    Column('location', VARCHAR(length=200)),
    Column('tweets', VARCHAR(length=3000)),
    Column('ranking', VARCHAR(length=20)),
    Column('rankscore', FLOAT),
    Column('ranktype', BOOLEAN),
)

twitter_ball = Table('twitter_ball', post_meta,
    Column('name', String(length=100), primary_key=True, nullable=False),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('tweets', String(length=3000)),
    Column('ranking', String(length=20)),
    Column('rankscore', Float),
    Column('ranktype', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['twitter_ball'].columns['location'].drop()
    post_meta.tables['twitter_ball'].columns['latitude'].create()
    post_meta.tables['twitter_ball'].columns['longitude'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['twitter_ball'].columns['location'].create()
    post_meta.tables['twitter_ball'].columns['latitude'].drop()
    post_meta.tables['twitter_ball'].columns['longitude'].drop()
