import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.api.models.certificate import CertificateCreate, CertificateStatus

@pytest.fixture
def client():
    return TestClient(app)

def test_create_certificate(client: TestClient):
    """Test certificate creation endpoint."""
    certificate_data = {
        "title": "Test Certificate",
        "description": "Test Description",
        "applicant_id": "test-123",
        "type": "technical",
        "requirements": ["req1", "req2"]
    }
    
    response = client.post(
        "/api/v1/certificates/",
        json=certificate_data
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == certificate_data["title"]
    assert data["status"] == CertificateStatus.PENDING.value

@pytest.mark.asyncio
async def test_get_certificate(client: TestClient, db_session):
    """Test getting a certificate by ID."""
    # Crear un certificado primero
    certificate_data = {
        "title": "Test Certificate",
        "description": "Test Description",
        "applicant_id": "test-123",
        "type": "technical",
        "requirements": ["req1", "req2"]
    }
    
    create_response = client.post(
        "/api/v1/certificates/",
        json=certificate_data
    )
    certificate_id = create_response.json()["id"]
    
    # Obtener el certificado
    response = client.get(f"/api/v1/certificates/{certificate_id}")
    assert response.status_code == 200
    assert response.json()["id"] == certificate_id