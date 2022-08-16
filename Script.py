class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {},
\nᴍʏ ɴᴀᴍᴇ ɪꜱ <a href=https://t.me/{}>{}</a> , ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇ ᴀɴᴅ sᴇʀɪᴇs,  ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ...😍
\nɴᴏᴛᴇ : ɪ ᴡᴏʀᴋ ᴏɴ ʙᴏᴛʜ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ​.</b>"""
    HELP_TXT = """<b>ʜᴇʏ {}
ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ꜰᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ</b>."""
    ABOUT_TXT = """<b>✯ ᴍʏ ɴᴀᴍᴇ: {}
✯ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/PenMovieHD>𝐏єη 𝐌๏νιє 𝐇ↁ</a>
✯ ʟɪʙʀᴀʀʏ: ᴘʏʀᴏɢʀᴀᴍ
✯ ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 𝟹
✯ ᴅᴀᴛᴀ ʙᴀꜱᴇ: ᴍᴏɴɢᴏ ᴅʙ
✯ ʙᴏᴛ ꜱᴇʀᴠᴇʀ: ʜᴇʀᴏᴋᴜ
✯ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ: v1.0.1 [ ʙᴇᴛᴀ ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
★ ᴛʜɪꜱ ɪꜱ ᴀ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ. 
★ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ - <a href=https://github.com/MyTGBotz/Movie>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>  

<b>DEVS:</b>
★ <a href=https://t.me/PenMovieHD>𝐏єη 𝐌๏νιє 𝐇ↁ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Mᴏᴠɪᴇ Pʀᴏᴠɪᴅᴇʀ 𝕏 will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Mᴏᴠɪᴇ Pʀᴏᴠɪᴅᴇʀ 𝕏 should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Mᴏᴠɪᴇ Pʀᴏᴠɪᴅᴇʀ 𝕏 Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Mᴏᴠɪᴇ Pʀᴏᴠɪᴅᴇʀ 𝕏 supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MovieProviderXBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Mᴏᴠɪᴇ Pʀᴏᴠɪᴅᴇʀ 𝕏

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
★ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> ᴍɪʙ
★ ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> ᴍɪʙ</b>"""
    LOG_TEXT_G = """<b>#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}</b>
"""
    LOG_TEXT_P = """<b>#NewUser
ID - <code>{}</code>
Name - {}</b>
"""
M_NT_FND = """<b>⭕️This Movie Is Not Found. \n\n⭕️Request For Uploading👇</b>"""
