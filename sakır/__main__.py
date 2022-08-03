# By < XnKiT >
# // SPAMMERBOT MADE BY (c) XNKIT™ //

import glob
from pathlib import Path
from sakır.utils import load_plugins
import logging
from . import worker


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "sakır/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴘʟᴏʏᴇᴅ!")
print("Başarlı bir şekilde deploy edildi Developer: @SakirBey1")
if __name__ == "__main__":
    worker.run_until_disconnected()
