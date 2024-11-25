import pytest
from unittest.mock import Mock, patch
from src.services.sambanova import SambanovaService
from src.api.models.certificate import CertificateCreate
from src.services.certificate_service import CertificateService

@pytest.mark.asyncio
async def test_sambanova_service():
    """Test SambaNova service document analysis."""
    service = SambanovaService()
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_response = Mock()
        mock_response.json.return_value = {"analysis": "test result"}
        mock_response.raise_for_status.return_value = None
        mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
        
        result = await service.analyze_document("test content")
        assert result["analysis"] == "test result"

@pytest.mark.asyncio
async def test_certificate_service(db_session):
    """Test certificate service operations."""
    sambanova_service = SambanovaService()
    service = CertificateService(db_session, sambanova_service)
    
    certificate_data = CertificateCreate(
        title="Test Certificate",
        description="Test Description",
        applicant_id="test-123",
        type="technical",
        requirements=["req1", "req2"]
    )
    
    # Test creation
    result = await service.create_certificate(certificate_data)
    assert result.title == certificate_data.title
    assert result.status == CertificateStatus.PENDING
