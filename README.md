# YouTube Downloader

Aplicación web para descargar videos y audio de YouTube en máxima calidad.

## Características

- ✅ Descarga videos en formato MP4 (hasta 4K)
- ✅ Descarga audio en formato M4A (AAC alta calidad)
- ✅ Interfaz web moderna y responsive
- ✅ Notificaciones modales elegantes
- ✅ Arquitectura limpia y profesional

## Arquitectura

```
src/
├── api/              # Endpoints de la API
│   ├── __init__.py
│   └── routes.py
├── models/           # Modelos de datos (DTOs)
│   ├── __init__.py
│   └── schemas.py
├── services/         # Lógica de negocio
│   ├── __init__.py
│   └── downloader.py
├── static/           # Archivos estáticos
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
├── utils/            # Utilidades
│   ├── __init__.py
│   ├── ffmpeg_finder.py
│   └── file_utils.py
├── views/            # Templates HTML
│   └── index.html
├── __init__.py
├── app.py            # Aplicación FastAPI
├── config.py         # Configuración
└── main.py           # Punto de entrada
```

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar la aplicación:
```bash
python -m src.main
```

O directamente:
```bash
python src/main.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://127.0.0.1:8000`

## Requisitos

- Python 3.8+
- FFmpeg (opcional, para mejor calidad de video)

## Tecnologías

- **FastAPI**: Framework web moderno y rápido
- **yt-dlp**: Descarga de videos de YouTube
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI

## Patrones de Diseño

- **Separation of Concerns**: Separación clara entre capas
- **Dependency Injection**: Servicios inyectables
- **Repository Pattern**: Abstracción de lógica de descarga
- **DTO Pattern**: Modelos de transferencia de datos
