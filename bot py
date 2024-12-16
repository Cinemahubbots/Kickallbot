from telethon import TelegramClient, errors

# Replace these with your API credentials and bot token
api_id = '22359038'
api_hash = 'b3901895dc193c30c808ba4f1b550ed0'
bot_token = '5685807128:AAFoTlc7eVbyQFyRRuZ_PpXF8Kmiz9weB8U'

# Replace this with your private channel invite link or ID
private_channel_invite = 'https://t.me/+YgHaqBswB6JmNjA1'

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
