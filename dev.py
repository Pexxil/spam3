from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/dev"))
async def repo(event):
    await event.reply("DELEVOPER",
                    buttons=[
                        [Button.url("MİRACBEY✓🇹🇷")]
                    ])
