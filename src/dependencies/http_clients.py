from collections.abc import AsyncGenerator

import httpx
from fast_depends import Depends

from config import Config, load_config_from_file

__all__ = ('get_http_client',)


async def get_http_client(
        config: Config = Depends(load_config_from_file),
) -> AsyncGenerator[httpx.AsyncClient]:
    async with httpx.AsyncClient(
            base_url=str(config.api_base_url),
    ) as http_client:
        yield http_client
