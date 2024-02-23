.SILENT:
.PHONY: default startapp

default: startapp

startapp:
	cd backend_fastapi && mkdir $(app) && cd $(app) && touch __init__.py schemas.py models.py && echo "from fastapi import APIRouter\n\n\nrouter = APIRouter(\n\tprefix=\"/$(app)\",\n\ttags=[\"$(app)\"]\n)\n\n\n@router.get(\"/\")\nasync def get_$(app)():\n\treturn \"default message from $(app)\"" > views.py
	cd backend_fastapi && echo "from .$(app).views import router as $(app)_router" >> __init__.py
	echo "router.include_router($(app)_router)" >> routers.py
