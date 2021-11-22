import os
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# read environment variables from .env
dotenv.read_dotenv(dotenv=os.path.join(BASE_DIR, ".envs/.django"))
dotenv.read_dotenv(dotenv=os.path.join(BASE_DIR, ".envs/.postgres"))

# set environment variables
WEBSITE_URL = os.getenv("WEBSITE_URL")
DATABASE_HOST = os.getenv("POSTGRES_DOCKER_HOST")
DATABASE_HOST = DATABASE_HOST if DATABASE_HOST else os.getenv("POSTGRES_HOST")
