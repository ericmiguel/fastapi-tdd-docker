"""Configurações."""

import logging
import os

from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Config(BaseSettings):
    """Modelo de configurações."""

    env: str = os.getenv("ENV", "dev")
    testing: bool = bool(os.getenv("TESTING", True))


@lru_cache()
def carregar_config() -> BaseSettings:
    """Carrega as configurações.

    Esta função é injetada na rota "pong". Carregar as configurações diretamente
    do código (ao invés de fazer a partir de um arquivo) é computacionalmente
    mais barato. Ainda assim, esta função é executada a cada requisição feita à
    rota "pong". Usaremos "lru_cache" para fazer com que a função seja executa
    apenas uma única vez.

    Veja a documentação oficial de "lru_cache" para mais detalhes:
    https://docs.python.org/3/library/functools.html#functools.lru_cache
    """
    log.info("Carregando as configurações de ambiente...")
    return Config()
