"""Servicio de descarga de videos"""
import yt_dlp
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.config import DOWNLOAD_FOLDER, MAX_VIDEO_HEIGHT
from src.utils import find_ffmpeg, sanitize_filename


class DownloaderService:
    """Servicio para descargar videos de YouTube"""
    
    def __init__(self):
        self.ffmpeg_path = find_ffmpeg()
    
    def _get_base_options(self, unique_id: str) -> Dict:
        """Obtiene las opciones base para yt-dlp"""
        opts = {
            'outtmpl': str(DOWNLOAD_FOLDER / f'{unique_id}.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'noplaylist': True,
        }
        
        if self.ffmpeg_path:
            opts['ffmpeg_location'] = self.ffmpeg_path
        
        return opts
    
    def _get_audio_options(self, unique_id: str) -> Dict:
        """Obtiene opciones para descarga de audio"""
        opts = self._get_base_options(unique_id)
        opts['format'] = 'bestaudio[ext=m4a]/bestaudio/best'
        return opts
    
    def _get_video_options(self, unique_id: str) -> Dict:
        """Obtiene opciones para descarga de video"""
        opts = self._get_base_options(unique_id)
        
        if self.ffmpeg_path:
            opts['format'] = f'bestvideo[ext=mp4][height<={MAX_VIDEO_HEIGHT}]+bestaudio[ext=m4a]/bestvideo+bestaudio/best'
            opts['merge_output_format'] = 'mp4'
        else:
            opts['format'] = f'best[ext=mp4][height<={MAX_VIDEO_HEIGHT}]/best'
        
        return opts
    
    def download(self, url: str, format_type: str, unique_id: str) -> Tuple[Path, str]:
        """
        Descarga un video o audio de YouTube.
        
        Args:
            url: URL del video
            format_type: Tipo de formato ('mp3' o 'mp4')
            unique_id: ID único para el archivo
            
        Returns:
            Tuple[Path, str]: Ruta del archivo descargado y nombre sanitizado
            
        Raises:
            Exception: Si ocurre un error durante la descarga
        """
        # Seleccionar opciones según formato
        if format_type == 'mp3':
            ydl_opts = self._get_audio_options(unique_id)
        else:
            ydl_opts = self._get_video_options(unique_id)
        
        # Descargar
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            
            # Buscar archivo descargado
            downloaded_files = list(DOWNLOAD_FOLDER.glob(f'{unique_id}.*'))
            
            if not downloaded_files:
                raise Exception("No se pudo descargar el archivo")
            
            file_path = downloaded_files[0]
            
            # Generar nombre de archivo
            title = info.get('title', 'video')
            safe_title = sanitize_filename(title)
            filename = f"{safe_title}.{file_path.suffix[1:]}"
            
            return file_path, filename
