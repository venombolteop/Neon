"""
MIT License

Copyright (c) 2023 TheHamkerCat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import asyncio
import time
from inspect import getfullargspec
from os import path

from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen
from Python_ARQ import ARQ
from telegraph import Telegraph


BOT_TOKEN="6037242990:AAH4yK1ovZwEnjT2yV22JYmNGXW3nOT9QEk" # Get it from @botfather

API_ID=22341875

API_HASH="b13c2392d55ae8a4800d3b4ed40bffb2"

SESSION_STRING="AgE7aHwAdQ3D6JtDLnTaNnqx0-nxtlvjZ6t_8MtkX1oJ8hZQ6ttEnHpUSNo0dQJDFHT-OQXDOx09hMOm9X9-_mKbGjbmyGQupz-xuGiTGNLDhsw5kwjVo1F-ivWavlPJq3T4e-VIgyt7y_weDFFPgCOM_mOCvLAQdlTGjeAy-MvDBUhxyjQtaU6ueietrqV34Cd260Vd_YPMqd7o-MKZk5Dbwvf7-tLqqtCsL6vNi8j_wQhNs6fv32tjQ0Ayik93uu9vVJlrXI6PNthPkIT9wsrW6XoWDJWm0kFymGtiHsMl-8OI9ucizP3mJHJ63uHD5LQw0aVvUIfvUv8AU6UKrdz0gvZWpAAAAAFr3-D8AA"

USERBOT_PREFIX="."

SUDO_USERS_ID=[5898049921] # Sudo users have full access to everythin, don't trust anyone

LOG_GROUP_ID=-1002064001274

MONGO_URL="mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority"

GBAN_LOG_GROUP_ID=-1002064001274

MESSAGE_DUMP_CHAT=-1002064001274

WELCOME_DELAY_KICK_SEC=300 # Edit if u want

ARQ_API_URL="https://arq.hamker.dev" # Leave it like this

ARQ_API_KEY="NDUZKA-EJDXBX-TJWGGO-MDTLCL-ARQ" # Get it from @ARQRobot

LOG_MENTIONS=1 # Make it 1 if you want to enable it

RSS_DELAY=300 # In seconds

PM_PERMIT=1

MOD_LOAD = []
MOD_NOLOAD = []
SUDOERS = filters.user()
bot_start_time = time.time()


class Log:
    def __init__(self, save_to_file=False, file_name="wbb.log"):
        self.save_to_file = save_to_file
        self.file_name = file_name

    def info(self, msg):
        print(f"[+]: {msg}")
        if self.save_to_file:
            with open(self.file_name, "a") as f:
                f.write(f"[INFO]({time.ctime(time.time())}): {msg}\n")

    def error(self, msg):
        print(f"[-]: {msg}")
        if self.save_to_file:
            with open(self.file_name, "a") as f:
                f.write(f"[ERROR]({time.ctime(time.time())}): {msg}\n")


log = Log(True, "bot.log")

# MongoDB client
log.info("Initializing MongoDB client")
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.wbb


async def load_sudoers():
    global SUDOERS
    log.info("Loading sudoers")
    sudoersdb = db.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    for user_id in SUDO_USERS_ID:
        SUDOERS.add(user_id)
        if user_id not in sudoers:
            sudoers.append(user_id)
            await sudoersdb.update_one(
                {"sudo": "sudo"},
                {"$set": {"sudoers": sudoers}},
                upsert=True,
            )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)


loop = asyncio.get_event_loop()
loop.run_until_complete(load_sudoers())

if not SESSION_STRING:
    app2 = Client(
        name="userbot",
        api_id=API_ID,
        api_hash=API_HASH,
        phone_number=PHONE_NUMBER,
    )
else:
    app2 = Client(
        "userbot",
        session_string=SESSION_STRING,
    )

aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

app = Client("wbb", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

log.info("Starting bot client")
app.start()
log.info("Starting userbot client")
app2.start()

log.info("Gathering profile info")
x = app.get_me()
y = app2.get_me()

BOT_ID = x.id
BOT_NAME = x.first_name + (x.last_name or "")
BOT_USERNAME = x.username
BOT_MENTION = x.mention
BOT_DC_ID = x.dc_id

USERBOT_ID = y.id
USERBOT_NAME = y.first_name + (y.last_name or "")
USERBOT_USERNAME = y.username
USERBOT_MENTION = y.mention
USERBOT_DC_ID = y.dc_id

if USERBOT_ID not in SUDOERS:
    SUDOERS.add(USERBOT_ID)

log.info("Initializing Telegraph client")
telegraph = Telegraph(domain="graph.org")
telegraph.create_account(short_name=BOT_USERNAME)


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
