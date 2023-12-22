from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

images_serve_router = APIRouter()


@images_serve_router.get("/{filename}", summary="Get an image", tags=["Images"])
async def get_image(filename: str):
    image_path = Path("path/to/your/image/directory") / filename
    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path)
