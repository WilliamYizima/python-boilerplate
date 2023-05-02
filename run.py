# import uvicorn
from src.main import main
import asyncio
import logging

if __name__ == "__main__":
    # Print Rocketry's logs to terminal
    logger = logging.getLogger("rocketry.task")
    logger.addHandler(logging.StreamHandler())

    asyncio.run(main())
