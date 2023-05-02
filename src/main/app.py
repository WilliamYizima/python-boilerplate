# from src.main.routes import main
import asyncio
import uvicorn
from src.main.framework.fastapi import app as app_fastapi
from src.config import config
from src.infra.scheduler import app as app_rocketry


class Server(uvicorn.Server):
    """Customized uvicorn.Server

    Uvicorn server overrides signals and we need to include
    Rocketry to the signals."""

    def handle_exit(self, sig: int, frame) -> None:
        app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    "Run Rocketry and FastAPI"

    server = Server(
        config=uvicorn.Config(
            app_fastapi, workers=1, loop="asyncio", port=int(config["PORT"])
        )
    )

    api = asyncio.create_task(server.serve())
    sched = asyncio.create_task(app_rocketry.serve())

    await asyncio.wait([sched, api])
