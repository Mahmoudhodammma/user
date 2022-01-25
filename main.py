import requests
import telebot
from telebot import types
import random
import os
import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
dev = types.InlineKeyboardButton(text="- Dev -",url="https://t.me/uufffuu")
start = types.InlineKeyboardButton(text="- Start ▶️",callback_data="s")
@bot.message_handler(commands=["start"])
def f(message):
	name = message.chat.first_name
	ur = "https://t.me/pydroi_d_3/34"
	key = types.InlineKeyboardMarkup()
	key.row_width=1
	key.add(start,dev)
	bot.send_photo(message.chat.id,ur,f"""
- Hello {name}
- Welcome Bot 
- Making Combo User&Pass
- Dev :-: @uufffuu""",reply_markup=key)
@bot.callback_query_handler(func=lambda call :True)
def f(call):
	if call.data=="s":
		st(call.message)
def st(message):
	m=0
	chat_id = str(message.chat.id)
	start = bot.send_message(message.chat.id, "Start ✅")
	u = "zxcvbnmlkjhgfdsaqwertyuiop__0987654321"
	es = "1020304050","10203040","123454321","200200","19981998","11223344","1122334455","987654321"
	for i in range(1300):
		m+=1
		ran = ''.join(random.choice(u)for i in range(4))
		ran1 = ''.join(random.choice(es)for i in range(1))
		with open("UserPass.txt","a") as mo:
			mo.write(f"{ran}:{ran1}\n")
		ins = types.InlineKeyboardButton(text=f"- User : {ran} 🔰",callback_data="sjdj")
		ch = types.InlineKeyboardButton(text=f"- Pass : {ran1} ⚠️",callback_data="dfjrhd")
		em = types.InlineKeyboardButton(text=f"- Number Combo : {m} 🔱",callback_data="sbncn")
		key = types.InlineKeyboardMarkup()
		key.row_width=1
		key.add(ins,ch,em)
		result = """
- Making Combo User&Pass 🔱
- Please Wait... ♻️
- Dev - @uufffuu , @bo0tt , @api_7"""
		bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id,reply_markup=key)
	file = open("UserPass.txt","r")
	bot.send_document((message.chat.id),file,caption=f"""
- - - - - - - - - - - - - - - - - -
- ᴅᴏɴᴇ ᴍᴀᴋɪɴɢ ᴄᴏᴍʙᴏ️ ✔️
- ᴄᴏᴍʙᴏ : User&Pass
- sɪᴢᴇ : {m}
- - - - - - - - - - - - - - - - - -
""",reply_to_message_id=(message.message_id))
	os.remove("UserPass.txt")
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://botuserpass.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
