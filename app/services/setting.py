from dotenv import load_dotenv
import os

load_dotenv()
TTL_TIME = int(os.getenv("TTL_TIME", 4))