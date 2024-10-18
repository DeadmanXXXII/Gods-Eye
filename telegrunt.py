from telethon.sync import TelegramClient

# Replace these with your Telegram API credentials
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone = 'your_phone_number'

# Initialize Telegram client
client = TelegramClient(phone, api_id, api_hash)
client.start()

# Monitor target public channel
target_channel = 'target_public_channel'
for message in client.iter_messages(target_channel):
    print(f"Sender ID: {message.sender_id}, Message: {message.text}")
