from fastapi import APIRouter


router = APIRouter(
	prefix="/game",
	tags=["game"]
)


@router.get("/")
async def get_game():
	return "default message from game"
