import httpx
from typing import Dict, Any
from src.config.settings import settings
import logging

logger = logging.getLogger(__name__)

class SambanovaService:
    def __init__(self):
        self.api_key = settings.SAMBANOVA_API_KEY
        self.base_url = settings.SAMBANOVA_BASE_URL
        self.model = settings.SAMBANOVA_MODEL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def analyze_document(self, content: str) -> Dict[str, Any]:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/analyze",
                    headers=self.headers,
                    json={
                        "model": self.model,
                        "content": content,
                        "options": {
                            "temperature": 0.7,
                            "max_tokens": 1000
                        }
                    }
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Error en SambaNova API: {str(e)}")
            raise
