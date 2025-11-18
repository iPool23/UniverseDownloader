"""Utilidades para manejo de archivos"""


def sanitize_filename(title: str, max_length: int = 50) -> str:
    """
    Limpia y sanitiza un título para usarlo como nombre de archivo.
    
    Args:
        title: Título original
        max_length: Longitud máxima del nombre
        
    Returns:
        str: Nombre de archivo sanitizado
    """
    # Reemplazar caracteres problemáticos
    title = title.replace('/', '-').replace('\\', '-')
    
    # Mantener solo caracteres alfanuméricos y algunos especiales
    safe_title = "".join(
        c for c in title 
        if c.isalnum() or c in (' ', '-', '_')
    ).strip()
    
    # Limitar longitud
    return safe_title[:max_length]
