from pyrogram import Client
from pyrogram.errors import FloodWait
import time

# Replace these with your own API details
API_ID = "22359038"
API_HASH = "b3901895dc193c30c808ba4f1b550ed0"
SESSION_NAME = "BQFVK_4AOurrGFrrXiK4rFj1YIZD5YhVPy4dA9K_rEmi8v62h7yJaQ26TVlF9alKRhWnrDMdU7az6DTlEaN8JpYkKq-E55gHfe2P12AiMG_pHYiPaHya-Ixd_qdDd87ikfn5ciJH4T3kKDJLiYvoLqI40Oat_UvLJVXNVp1Y4b8_BJ2egPDh5ImiiaRRkBJttuk-St85pYqFZ63aN3-yzYif2Uk1Xxa_J6g0MsY7uSk9gporRmS85MJVwzZJVZ_mYJC94Isr9l6zOGTsikNhkk_o7XziPbaCR4gTE1lm-RYtKZYp98uS0aQT3Q9ZZPuERh0av_qLcadA_DoGmEcQYLi70NToBwAAAAFJs2jlAA"  # Can be any session name

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
