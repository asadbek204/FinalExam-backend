from fastapi import APIRouter


router = APIRouter(
	prefix="/history",
	tags=["history"]
)


@router.get("/")
async def get_history():
	return "default message from history"
