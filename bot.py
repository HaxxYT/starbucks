import os
import random
import asyncio
import threading
import time
from datetime import datetime, timedelta
from collections import defaultdict

import discord
from discord.ext import commands
from dotenv import load_dotenv
from faker import Faker
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

# Load .env file if running locally
load_dotenv()

# ---------- Configuration ----------
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CAPSOLVER_API_KEY = os.getenv("CAPSOLVER_API_KEY")
PROXY_URLS = [p.strip() for p in os.getenv("PROXY_URL", "").split(",") if p.strip()]

# Validate required tokens (fail fast)
if not DISCORD_TOKEN:
    raise ValueError("Missing DISCORD_TOKEN environment variable")
if not CAPSOLVER_API_KEY:
    raise ValueError("Missing CAPSOLVER_API_KEY environment variable")

CONTACT_URL = "https://customercare.starbucks.co.uk/sbux?id=contact&lang=en"
HEADLESS = True   # Keep True on Railway
SLOW_MO = 20

# ... rest of your code (generate_complaint, solve_captcha, etc.)
# Make sure to keep all functions as you wrote them.

# At the very bottom:
bot.run(DISCORD_TOKEN)
