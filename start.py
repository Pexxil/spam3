# By < Miraç Bey >
# // SPAMMERBOT MADE BY (c) MiraçBey™ //

from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("ѕοмє ιиƒο αϐουτ οωиєя.",
                    buttons=[
                        [Button.url("οωиєя", url="https://t.me/KadimmTayfa")],
                        [Button.inline("Kontrol et✓",data="op")]
                    ])

@worker.on(events.callbackquery.CallbackQuery(data="op"))
async def ex(event):
    await event.edit("Bunu yaz /help",
                    buttons=[
                        [Button.url("οωиєя", url="https://t.me/beylerbeyiniz")]
                    ])


