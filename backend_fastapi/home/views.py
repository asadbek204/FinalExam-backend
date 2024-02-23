from fastapi import APIRouter


router = APIRouter(
	prefix="/home",
	tags=["home"]
)


@router.get("/")
async def get_home():
	return "default message from home"
