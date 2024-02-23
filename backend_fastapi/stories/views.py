from fastapi import APIRouter


router = APIRouter(
	prefix="/stories",
	tags=["stories"]
)


@router.get("/")
async def get_stories():
	return "default message from stories"
