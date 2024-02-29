from fastapi import APIRouter


router = APIRouter(
	prefix="/payment",
	tags=["payment"]
)


@router.get("/")
async def get_wallet():
	return "default message from payment"
