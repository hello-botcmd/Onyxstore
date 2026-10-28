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


DATABASE_URL = "mongodb+srv://nexacoders2_db_user:dxYh7QOdHvH6OVdd@cluster0.f4qxcbk.mongodb.net/?appName=Cluster0")                       # your own MongoDB for THIS bot
             # Quick Codes API address, e.g. https://api.example.com



ADMIN_IDS = [8580367479]
DB_NAME = "reseller_bot"

QC_API_BASE = "https://YOUR-QUICK-CODES-API-URL".rstrip("/")

BOT_TITLE = "NFT STACKS STORE"
SUPPORT_LINK = "https://t.me/nftstacks"UPPORT_LINK", "https://t.me/nftstacks").strip()      # optional "Contact Support" button on payment problems
