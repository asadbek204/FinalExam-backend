from fastapi import APIRouter


router = APIRouter(
	prefix="/group",
	tags=["group"]
)


@router.get("/")
async def get_group():
	return "default message from group"
