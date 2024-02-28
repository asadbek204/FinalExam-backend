from fastapi import APIRouter


router = APIRouter(
	prefix="/archive",
	tags=["archive"]
)


@router.get("/")
async def get_archive():
	return "default message from archive"
