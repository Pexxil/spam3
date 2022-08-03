import asyncio
import os
from .. import worker, BOT_USERS, BOT_USER, LOGGER_GROUP
from asyncio import wait
from telethon import events
LOGGER_GROUP = int(os.environ.get("LOGGER_GROUP", None))
import re
abcd = "@beylerbeyiniz@KadimmTayfaa"
x = "@beylerbeyiniz"
king = [2127221861]

@worker.on(events.NewMessage(incoming=True, pattern="/bigspam"))
async def bigspam(e):
  users = BOT_USERS
  if not str(e.sender_id) in users:
    return await e.reply("ᴋɪᴅ ʏᴏᴜ ʜᴀᴠᴇ ɴᴏ ᴄᴏɴᴛʀᴏʟ ᴏɴ ᴍᴇ (sᴇᴅ)")
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
    await asyncio.sleep(0.01)
  if re.search(abcd.lower(), e.text.lower()):
    return await e.reply("ᴍᴀᴀᴄʜᴜᴅᴀ ᴛᴜ,[ Wᴏ ᴏᴡɴᴇʀ ʜᴀɪ ]")
  if not e.text in abcd:
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#ʙɪɢsᴘᴀᴍ\n"
                        + f"ʙɪɢsᴘᴀᴍ ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ɪɴ {(e.chat.title)} (`{e.chat_id}`) ᴡɪᴛʜ {counter} ᴛɪᴍᴇs ᴡɪᴛʜ {e.text}",
                    )

@worker.on(events.NewMessage(incoming=True, pattern="/spam"))
async def spammer(e):
  users = BOT_USERS
  if not str(e.sender_id) in users:
    return await e.reply("Kontrolümde değilsin✓")
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
    await asyncio.sleep(0.01)
  if re.search(abcd.lower(), e.text.lower()):
    return await e.reply("ᴍᴀᴀᴄʜᴜᴅᴀ ᴛᴜ,[ Wᴏ ᴏᴡɴᴇʀ ʜᴀɪ ]")
  if not e.text in abcd:
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#sᴘᴀᴍ\n"
                        + f"sᴘᴀᴍ ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ɪɴ {(e.chat.title)} (`{e.chat_id}`) ᴡɪᴛʜ {counter} ᴛɪᴍᴇs ᴡɪᴛʜ {e.text}",
                    )

@worker.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspammer(e):
  if not str(e.sender_id) in BOT_USERS:
    return await e.reply("Kontrolümde değilsin✓")
  if (abcd.lower()) in (e.text.lower()):
    return await e.reply("ᴍᴀᴀᴄʜᴜᴅᴀ ᴛᴜ,[ Wᴏ ᴏᴡɴᴇʀ ʜᴀɪ ]")
  else:
      xD = e.text[7:]
      a = 1
      while a == 1:
        await e.client.send_message(e.chat, xD)
        await asyncio.sleep(1.95)

@worker.on(events.NewMessage(incoming=True, pattern="/mspam"))
async def tiny_pic_spam(e):
  if not str(e.sender_id) in BOT_USERS:
    return await e.reply("Kontrolümde değilsin✓")
  if str(e.sender_id) in BOT_USERS:
    try:
      reply = await e.get_reply_message()
    except:
      await event.respond("sᴏᴍᴇᴛʜɪɴɢ ɢᴇᴛᴛɪɴɢ ᴡʀᴏɴɢ")
      return "ғᴜᴄᴋ ᴏғғ"
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        media = await e.client.download_media(reply)
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, media)
        await e.delete()
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#ᴍᴇᴅɪᴀsᴘᴀᴍ\n"
                        + f"ᴍᴇᴅɪᴀ sᴘᴀᴍ ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ɪɴ {(e.chat.title)} (`{e.chat_id}`) ᴡɪᴛʜ {counter} ᴛɪᴍᴇs ᴡɪᴛʜ {e.text}",
                    )


@worker.on(events.NewMessage(incoming=True, pattern="/restart"))
async def restart(e):
  if not str(e.sender_id) in BOT_USERS:
    return await e.reply("ᴋɪᴅ ʏᴏᴜ ʜᴀᴠᴇ ɴᴏ ᴄᴏɴᴛʀᴏʟ ᴏɴ ᴍᴇ (sᴇᴅ)")
  if str(e.sender_id) in BOT_USERS:
    try:
        text = "ʀᴇsᴛᴀʀᴛᴇᴅ\n\nWᴀɪᴛ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs 😬😲😬..."
        await e.reply(text, parse_mode=None, link_preview=None)
        await worker.disconnect()
    except Exception:
        pass
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
