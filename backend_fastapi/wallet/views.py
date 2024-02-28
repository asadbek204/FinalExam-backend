from fastapi import APIRouter


router = APIRouter(
	prefix="/wallet",
	tags=["wallet"]
)


@router.get("/")
async def get_wallet():
	return "default message from wallet"
