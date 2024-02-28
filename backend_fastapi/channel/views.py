from fastapi import APIRouter


router = APIRouter(
	prefix="/channel",
	tags=["channel"]
)


@router.get("/")
async def get_channel():
	return "default message from channel"
