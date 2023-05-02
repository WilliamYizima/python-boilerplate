import os
from dotenv import load_dotenv

load_dotenv()

dirname = os.path.dirname(__file__)

config = {}
config["SCHED_TIME"] = os.environ.get("SCHED_TIME", "04:00")
config["PORT"] = os.environ.get("PORT", 9001)
