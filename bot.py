from telethon import TelegramClient, errors

# Replace these with your API credentials and bot token
api_id = '22359038'
api_hash = 'b3901895dc193c30c808ba4f1b550ed0'
bot_token = '6405574355:AAESGO5kXViYoDLC6rgaITEFJOzacsuwJM0'
# Replace this with your private channel invite link or ID
async def get_channel_id():
    channel = await client.get_entity("https://t.me/+uVNNnsoim7RiNjNl")
    print(f"Channel ID: {channel.id}")

# Initialize the Telegram client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

async def kick_all_members(channel_link):
    try:
        # Resolve the private channel entity
        channel = await client.get_entity(channel_link)
        
        # Iterate over all participants in the channel
        async for user in client.iter_participants(channel):
            if user.bot:  # Skip kicking other bots
                continue
            try:
                print(f"Kicking user: {user.id}")
                await client.kick_participant(channel, user.id)  # Remove the user
            except errors.UserAdminInvalidError:
                print(f"Cannot kick admin: {user.id}")
            except Exception as e:
                print(f"Error kicking user {user.id}: {e}")
    except Exception as e:
        print(f"Error accessing the channel: {e}")

async def main():
    await kick_all_members(private_channel_invite)

# Run the script
with client:
    client.loop.run_until_complete(main())
