from backend_fastapi import *
from fastapi import APIRouter
router = APIRouter()
router.include_router(auth_router)
router.include_router(home_router)
router.include_router(live_router)
router.include_router(profile_router)
router.include_router(chat_router)
router.include_router(channel_router)
router.include_router(game_router)
router.include_router(search_router)
router.include_router(wallet_router)
router.include_router(market_router)
router.include_router(group_router)
