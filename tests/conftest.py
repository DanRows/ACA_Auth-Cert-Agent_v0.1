import pytest
import asyncio
from typing import Generator, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from fastapi.testclient import TestClient
from src.database.models import Base
from src.main import app
from src.config.settings import settings
from src.services.sambanova import SambanovaService