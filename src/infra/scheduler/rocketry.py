"""
rocketry is a Scheduler
tasks:
    - get src_data and copy to temp-data
    - get data in temp-data and upload azure blob
    - delete temp-data files
"""
from loguru import logger
from rocketry import Rocketry
from rocketry.conds import daily
from src.config import config

# from rocketry.conds import after_success, after_all_finish, after_fail


app = Rocketry(config={"task_execution": "async"})

"""
write about your pipelione
"""


@app.task("every 2 second", name="task_teste")
async def task_test_2_secs():
    logger.info("Testando")
    return "Teste"


@app.task(daily.at(config["SCHED_TIME"]), name="task_teste_env")
async def task_teste_env():
    print("Init process in tasks")
    """ insert your use_case """
    logger.info("Testando ENV")
    return "Teste"
