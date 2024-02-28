from fastapi import APIRouter


router = APIRouter(
	prefix="/market",
	tags=["market"]
)


@router.get("/")
async def get_market():
	return "default message from market"
