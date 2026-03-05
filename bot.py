from telethon import TelegramClient, events
import asyncio

api_id = 37587908
api_hash = "e41cd61fdc76ca3cc4dd398d85272069"

source_channel = ["opfswk4351","minkhant808","allcarnandaw","deedeehd1234","goldlay999"]
target_channel = "myakalay33"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await asyncio.sleep(8)
    await event.message.forward_to(target_channel)

client.start()
print("Bot Running")
client.run_until_disconnected()
