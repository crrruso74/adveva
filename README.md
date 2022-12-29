<p align="center">
  <img src="assets/logo.jpg" alt="AM-ROBOTS">
</p>
<h1 align="center">
  <b>Eva Maria Bot</b>
</h1>


[![Stars](https://img.shields.io/github/stars/AM-ROBOTS/EvaMaria?style=flat-square&color=yellow)](https://github.com/AM-ROBOTS/EvaMaria/stargazers)
[![Forks](https://img.shields.io/github/forks/AM-ROBOTS/EvaMaria?style=flat-square&color=orange)](https://github.com/AM-ROBOTS/EvaMaria/fork)
[![Size](https://img.shields.io/github/repo-size/AM-ROBOTS/EvaMaria?style=flat-square&color=green)](https://github.com/AM-ROBOTS/EvaMaria/)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/AM-ROBOTS/EvaMaria)   
[![Contributors](https://img.shields.io/github/contributors/AM-ROBOTS/EvaMaria?style=flat-square&color=green)](https://github.com/AM-ROBOTS/EvaMaria/graphs/contributors)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/AM-ROBOTS/EvaMaria/blob/main/LICENSE)
[![Sparkline](https://stars.medv.io/AM-ROBOTS/EvaMaria.svg)](https://stars.medv.io/AM-ROBOTS/EvaMaria)


## Features

- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] File Store
## Variables

Read [this](https://telegram.dog/AmRobots_Bots/56) before you start messing up with your edits.

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/h9QjSSmk5tw)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/h9QjSSmk5tw)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* Check [info.py](https://github.com/AM-ROBOTS/EvaMaria/blob/master/info.py) for more


## Deploy
You can deploy this bot anywhere.

<i>**[Watch Deploying Tutorial...](https://youtu.be/Miajl2amrKo)**</i>

<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://telegram.dog/XTZ_HerokuBot?start=QU0tUk9CT1RTL0V2YU1hcmlhIG1haW4">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/AM-ROBOTS/EvaMaria
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>


## Commands
```
logs - to get the rescent errors
stats - to get status of files in db.
filter - add manual filters
filters - view filters
connect - connect to PM.
disconnect - disconnect from PM
del - delete a filter
delall - delete all filters
deleteall - delete all index(autofilter)
delete - delete a specific file from index.
info - get user info
id - get tg ids.
imdb - fetch info from imdb.
users - to get list of my users and ids.
chats - to get list of the my chats and ids 
index  - to add files from a channel
leave  - to leave from a chat.
disable  -  do disable a chat.
enable - re-enable chat.
ban  - to ban a user.
unban  - to unban a user.
channel - to get list of total connected channels
users_broadcast - to broadcast a message to all AM-ROBOTS users
groups_broadcast - to broadcast a message to all AM-ROBOTS groups
batch - to create link for multiple posts
link - to create link for one post
```
## Support
[![telegram badge](https://img.shields.io/badge/Telegram-Group-30302f?style=flat&logo=telegram)](https://telegram.dog/AmRobots_Support)
[![telegram badge](https://img.shields.io/badge/Telegram-Channel-30302f?style=flat&logo=telegram)](https://telegram.dog/AmRobots_Bots)

## Credits 
* [![AM-ROBOTS-Devs](https://img.shields.io/static/v1?label=AM-ROBOTS&message=devs&color=critical)](https://telegram.dog/AM_ROBOTS)


## Thanks to 
 - Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)
 - Thanks To All Everyone In This Journey

### Note

[Note To A So Called Dev](https://telegram.dog/AmRobots_Bots/56): 

## Disclaimer
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 2.0.](https://github.com/AM-ROBOTS/EvaMaria/blob/master/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.

## Inspiration
This is an attempt to create a clone of a BOAT made out of [banana trees 🌳](https://telegram.dog/GetTGLink/4187)

[![For Vaza](https://telegra.ph/file/e743b0c8a04252774bac2.jpg)](https://telegra.ph/file/98342dc186fd7484cba91.mp4 "Oru Kootam Vazhakalk samarpikkunnu")
