from fastapi import APIRouter


router = APIRouter(
	prefix="/live",
	tags=["live"]
)


@router.get("/")
async def get_live():
	return "default message from live"
