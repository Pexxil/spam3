# By < XNKIT >
# // SPAMMERBOT MADE BY ©XNKIT™ //


from . import *
from .. import worker as sakir, ALIVE_NAME
from telethon import events, Button


ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "ᴀɴᴋɪᴛ 🇮🇳 [ᴏꜰꜰʟɪɴᴇ]™"

@sakir.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    tatti=f"Sᴘᴀᴍᴍᴇʀ Bᴏᴛ Fᴏʀ {ALIVE_NAME} \nMᴀᴅᴇ Bʏ @XnKiTKuMaR"
    await event.reply(tatti,
                    buttons=[
                        [Button.inline("cհҽϲκ мє",data="helpme")]
                    ])

@sakir.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="ι Aᴍ Sᴘᴀᴍᴍᴇʀ Bᴏᴛ!\nι Cᴀɴ Sᴘᴀᴍ Fᴏʀ Mʏ Mᴀsᴛᴇʀ.\n\nTʀʏ Mᴇ!! Rᴇϙᴜᴇsᴛ Cᴏᴅᴇ ɪɴ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ!"
    await event.edit(text,
                     buttons=[
                         [Button.inline("ιиƒο", data="lu")],
                         [Button.inline("ϲοммαи∂ѕ", data="2")],
                         [Button.inline("ϲℓοѕє", data="3")]
                     ])

@sakir.on(events.callbackquery.CallbackQuery(data="2"))
async def ex(event):
    uuu="ϲοммαи∂ѕ ϐυττοиѕ ϐєℓοω "
    await event.edit(uuu,
                     buttons=[
                         [Button.inline("ѕραм", data="spam")],
                         [Button.inline("ϐιgѕραм", data="bigspam")],
                         [Button.inline("υѕραм", data="uspam")],
                         [Button.inline("мѕραм", data="mspam")],
                         [Button.inline("ϐαϲκ", data="helpme")]
                     ])

@sakir.on(events.callbackquery.CallbackQuery(data="3"))
async def ex(event):
    text3="мєиυ нαѕ ϐєєи ϲℓοѕє∂."
    await event.edit(text3,
                     buttons=[
                         [Button.inline("яєορєи", data="helpme")]
                     ])

@sakir.on(events.callbackquery.CallbackQuery(data="lu"))
async def ex(event):
    text4="ѕοмє ιиƒο."
    await event.edit(text4,
                     buttons=[
                         [Button.url("Wᴇʙsɪᴛᴇ", url="https://xnkit.github.io/k")],
                         [Button.url("ɢɪᴛʜᴜʙ", url="https://github.com/XnKiT")],
                         [Button.url("ᴛᴇʟᴇɢʀᴀᴍ", url="https://t.me/XnKiTKuMaR")],
                         [Button.inline("ʙᴀᴄᴋ", data="helpme")]
                     ])

@sakir.on(events.callbackquery.CallbackQuery(data="spam"))
async def ex(event):
    texi="➽ /spam number text \nMaximum /spam 99 text."
    await event.edit(texi,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="2")]
                     ])

@sakir.on(events.callbackquery.CallbackQuery(data="bigspam"))
async def ex(event):
    tut="➽ /bigspam number text \nMinimum /bigspam 101 text \nMaximum /bigspam 9999 text."
    await event.edit(tut,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="2")]
                     ])

@sakir.on(events.callbackquery.CallbackQuery(data="uspam"))
async def ex(event):
    tempu="➽ /uspam text \nNo LimiT \nJust Do /restart to stop."
    await event.edit(tempu,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="2")]
                     ])

@sakir.on(events.callbackquery.CallbackQuery(data="mspam"))
async def ex(event):
    achdh="➽ tag any media & Do /mspam number \nLiMiT Depend on number \nJust Do /restart to stop."
    await event.edit(achdh,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="2")]
                     ])
