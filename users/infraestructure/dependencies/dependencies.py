from dependency_injector import containers, providers
from users.core.providers.mysql import Connector, DBConnection


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    dbService = providers.Singleton(
        Connector,
        host=config.dbhost,
        database=config.database,
        user=config.dbuser,
        password=config.dbpassword,
        port=config.dbport,
    )
    service = providers.Factory(
        DBConnection,
        connector=dbService,
    )
