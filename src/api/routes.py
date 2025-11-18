"""Rutas de la API"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import uuid
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.models import DownloadRequest
from src.services import DownloaderService

router = APIRouter(prefix="/api", tags=["download"])
downloader = DownloaderService()


@router.post("/download")
async def download_video(request: DownloadRequest):
    """
    Descarga un video o audio de YouTube.
    
    Args:
        request: Datos de la solicitud de descarga
        
    Returns:
        FileResponse: Archivo descargado
        
    Raises:
        HTTPException: Si ocurre un error durante la descarga
    """
    try:
        unique_id = str(uuid.uuid4())[:8]
        file_path, filename = downloader.download(
            url=request.url,
            format_type=request.format,
            unique_id=unique_id
        )
        
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type='application/octet-stream'
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
