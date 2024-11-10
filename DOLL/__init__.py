from DOLL.core.bot import Sona
from DOLL.core.dir import dirr
from DOLL.core.git import git
from DOLL.core.userbot import Userbot
from DOLL.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sona()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
