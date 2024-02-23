from fastapi import APIRouter


router = APIRouter(
	prefix="/auth",
	tags=["auth"]
)


@router.get("/")
async def get_auth():
	return "default message from auth"
