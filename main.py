import uvicorn

from src.settings import settings

if __name__ == '__main__':
    uvicorn.run(
        'src.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=settings.reload
    )
