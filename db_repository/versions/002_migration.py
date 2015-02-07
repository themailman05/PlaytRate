from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
place_ranking = Table('place_ranking', post_meta,
    Column('name', String(length=120), primary_key=True, nullable=False),
    Column('location', String(length=200)),
    Column('computedrating', Float(precision=12)),
    Column('yelprating', Float(precision=12)),
    Column('quips', String(length=280)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['place_ranking'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['place_ranking'].drop()
