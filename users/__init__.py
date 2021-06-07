"""Project package."""
from .infraestructure.dependencies.dependencies import Container
from users_api.settings import base
from users.core.repository.user import user

container = Container()
container.config.from_dict(base.__dict__)
container.wire(modules=[user])
