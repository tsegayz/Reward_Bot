from typing import Final
from telegram import Update, Bot
from telegram.ext import  Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN: Final = '6890618870:AAFiVEaM5_LntbXhJmpXxyYEk295NvQ783M'
BOT_USERNAME: Final = '@group_growth_rewardbot'
GROUP_CHAT_ID = "group_id"
user_invites = {}

bot = Bot(token=TOKEN)
# this is the first message the user gets when the start command is clicked
async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello, Welcome to the group!")

# this the function to guide users understand how the bot works
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("welcone here you can invite your contacts to join and earn rewards.")

#this is the function that checks if the user added contacts to the group and provides reward
async def invite_command(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    # Checking if a user is in the group
    chat_member = await context.bot.get_chat_member(GROUP_CHAT_ID, user_id)

    if chat_member.status == 'member':
        # Check if the user has actually invited someone before incrementing invites
        if user_id in user_invites:
            user_invites[user_id] += 1
            await update.message.reply_text(f"Congratulations! You've earned a reward for inviting {user_id.first_name} to the group. Total invites: {user_invites[user_id]}")
        else:
            invite_link = 'https://t.me/+xutown9xFzNiOTc0'  
            await update.message.reply_text(f'You haven\'t invited anyone yet. Please invite someone to the group first. You can join the group using this [link]({invite_link}).', parse_mode='Markdown')
    else:
        invite_link = 'https://t.me/+xutown9xFzNiOTc0' 
        await update.message.reply_text(f'You must first join our group. You can join the group using this [link]({invite_link}).', parse_mode='Markdown')


if __name__ == '__main__':

    print('starting bot .......')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("invite", invite_command))  
    # app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, gainReward_command))

    app.run_polling(poll_interval=3)
