# By < XnKiT >
# // SPAMMERBOT MADE BY (c) XNKIT™ //

import sys
import logging
import importlib
from telethon import TelegramClient, events
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"sakır/plugins/{plugin_name}.py")
    name = "sakır.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["sakır.plugins." + plugin_name] = load
    print("sᴘᴀᴍᴍᴇʀ ʙᴏᴛ ʜᴀs ɪᴍᴘᴏʀᴛᴇᴅ " + plugin_name)
