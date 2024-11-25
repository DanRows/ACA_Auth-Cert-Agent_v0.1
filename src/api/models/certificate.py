from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from src.api.models.certificate import Certificate, CertificateCreate, CertificateUpdate
from src.services.certificate_service import CertificateService
from src.api.dependencies import get_certificate_service

router = APIRouter()

@router.post("/", response_model=Certificate)
async def create_certificate(
    certificate: CertificateCreate,
    service: CertificateService = Depends(get_certificate_service)
):
    return await service.create_certificate(certificate)

@router.get("/{certificate_id}", response_model=Certificate)
async def get_certificate(
    certificate_id: int,
    service: CertificateService = Depends(get_certificate_service)
):
    certificate = await service.get_certificate(certificate_id)
    if not certificate:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Certificate not found"
        )
    return certificate

@router.put("/{certificate_id}", response_model=Certificate)
async def update_certificate(
    certificate_id: int,
    certificate_update: CertificateUpdate,
    service: CertificateService = Depends(get_certificate_service)
):
    return await service.update_certificate(certificate_id, certificate_update)
