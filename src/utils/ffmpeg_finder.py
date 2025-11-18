"""Utilidad para encontrar FFmpeg en el sistema"""
import os
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.config import FFMPEG_LOCATIONS


def find_ffmpeg() -> Optional[str]:
    """
    Busca FFmpeg en ubicaciones comunes del sistema.
    
    Returns:
        str: Ruta al directorio de FFmpeg si se encuentra, None en caso contrario
    """
    for location in FFMPEG_LOCATIONS:
        if 'CapCut' in location and os.path.exists(location):
            # Búsqueda recursiva en CapCut
            for root, dirs, files in os.walk(location):
                if 'ffmpeg.exe' in files:
                    return root
        elif os.path.exists(os.path.join(location, 'ffmpeg.exe')):
            return location
    
    return None
