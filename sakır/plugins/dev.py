from .. import worker as sakir
from telethon import events, Button

@sakir.on(events.NewMessage(incoming=True, pattern="/dev"))
async def repo(event):
    await event.reply("ɪɴғᴏ ᴀʙᴏᴜᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ",
                    buttons=[
                        [Button.url("ᴀɴᴋɪᴛ 🇮🇳", url="https://xnkit.github.io/k")]
                    ])
