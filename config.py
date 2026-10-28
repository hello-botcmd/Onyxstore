# ============================================================================
# Copyright © 2026 Valrik Thakur (@valriks)
#
# Created & Developed by: Valrik Thakur
# Brand / Network: VTH NETWORK (@vthchannel)
#
# This source code is proprietary content created by Valrik Thakur.
# Unauthorized removal, modification, replacement, or concealment of the
# original author/brand credits is strictly prohibited.
#
# Redistribution, resale, rebranding, or claiming this work as your own
# without explicit permission from the author is prohibited.
#
# Any authorized use or modification must retain this copyright notice
# and the original author/brand credits.
#
# Created by Valrik Thakur | @valriks
# Powered by VTH NETWORK | @vthchannel
# ============================================================================


import os
from dotenv import load_dotenv

load_dotenv()


def _need(name):
    v = os.getenv(name, "").strip()
    if not v:
        raise RuntimeError(f"Missing required setting in .env: {name}")
    return v


BOT_TOKEN = _need("9080776064:AAGXvM4Ou5VLQ9_wcivu2JDrGwovl47RKoY")
ADMIN_IDS = [int(x) for x in _need("ADMIN_IDS").replace(" ", "8580367479").split(",") if x]
DATABASE_URL = _need("mongodb+srv://nexacoders2_db_user:dxYh7QOdHvH6OVdd@cluster0.f4qxcbk.mongodb.net/?appName=Cluster0")                       # your own MongoDB for THIS bot
DB_NAME = os.getenv("DB_NAME", "reseller_bot")
QC_API_BASE = _need("").rstrip("/")             # Quick Codes API address, e.g. https://api.example.com

BOT_TITLE = os.getenv("BOT_TITLE", "NFT STACKS STORE")   # name shown on the home screen
SUPPORT_LINK = os.getenv("SUPPORT_LINK", "https://t.me/nftstacks").strip()      # optional "Contact Support" button on payment problems
