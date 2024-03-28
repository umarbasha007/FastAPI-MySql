from enum import Enum
import os

from pydantic import BaseModel
from loguru import logger

from typing import Dict, Optional, List


class Environment(str, Enum):
    local = "local"
    dev = "dev"
    prod = "prod"


class Configuration(BaseModel):
    environment: Environment = Environment.local
    debug: bool = False
    database_url: str = os.environ.get("DATABASE_URL")
    secret_key: str = os.environ.get("SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24 * 8
    server_port: int = 8000
    server_host: str = "0.0.0.0"
    log_level: str = "INFO"


ENV_LOCAL = Configuration(
    environment=Environment.local,
    debug=True,
    database_url="sqlite:///./test.db",
    secret_key="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3",
)

ENV_DEV = Configuration(
    environment=Environment.dev,
    debug=True,
    database_url="sqlite:///./test.db",
)

ENV_PROD = Configuration(
    environment=Environment.prod,
    debug=False,
    database_url="sqlite:///./test.db",
)


DEFAULTS = {
    Environment.local: ENV_LOCAL,
    Environment.dev: ENV_DEV,
    Environment.prod: ENV_PROD,
}

env = Environment[os.getenv("ENVIRONMENT", Environment.local.value)]

cfg = DEFAULTS[env]

for k, v in cfg.dict().items():
    logger.info("{} : {}", k, v)


# logger.remove()
# logger.add(sys.stderr, level=config.log_level)
