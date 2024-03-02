from fastapi import APIRouter


router = APIRouter(
	prefix="/bot",
	tags=["bot"]
)


@router.get("/")
async def get_bot():
	return "default message from bot"
