"""Principal."""

from typing import Dict
from typing import Union

from app.config import Config
from app.config import carregar_config
from fastapi import Depends
from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
async def pong(
    config: Config = Depends(carregar_config),
) -> Dict[str, Union[str, bool]]:
    """
    Checagem de serviço.

    **Dependency injection**
    Note o "config: Config = Depends(carregar_config)" acima. A função "Depends" é uma
    dependência que declara outra dependência. Em outras palavras, "Depends" depende do
    resultado de "carregar_config". O valor retornado por "carregar_config" é retornado
    ao parâmetro "config" da rota "pong".

    Para mais detalhes, veja a documentação oficial:
    https://fastapi.tiangolo.com/tutorial/dependencies/

    Returns
    -------
    Dict[str, Union[str, bool]]
        pong e outras informações sobre o ambiente.
    """
    return {"ping": "pong!", "environment": config.env, "testing": config.testing}
