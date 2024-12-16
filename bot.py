from pyrogram import Client
from pyrogram.errors import FloodWait
import time

# Replace these with your own API details
API_ID = "your_api_id"
API_HASH = "your_api_hash"
SESSION_NAME = "my_userbot"  # Can be any session name

# Initialize the Pyrogram client
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

async def kick_all_members(channel_username):
    async with app:
        async for member in app.get_chat_members(channel_username):
            try:
                # Skip if the member is an admin or the creator
                if member.status in ["administrator", "creator"]:
                    print(f"Skipping admin: {member.user.first_name}")
                    continue

                # Kick the member
                await app.kick_chat_member(channel_username, member.user.id)
                print(f"Kicked: {member.user.first_name} (ID: {member.user.id})")
                time.sleep(1)  # Respect rate limits

            except FloodWait as e:
                print(f"FloodWait: Sleeping for {e.value} seconds")
                time.sleep(e.value)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    target_channel = input("Enter the username or ID of the channel: ")
    app.run(kick_all_members(target_channel))
