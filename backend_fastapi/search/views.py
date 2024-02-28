from fastapi import APIRouter


router = APIRouter(
	prefix="/search",
	tags=["search"]
)


@router.get("/")
async def get_search():
	return "default message from search"
