from typing import Final
from telegram import Update
from telegram.ext import  Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN: Final = '6890618870:AAFiVEaM5_LntbXhJmpXxyYEk295NvQ783M'
BOT_USERNAME: Final = '@group_growth_rewardbot'
GROUP_CHAT_ID = -123456789

# this is the first message the user gets when the start command is clicked
async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello, Welcome to the group!")

# this the function to guide users understand how the bot works
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("welcone here you can invite your contacts to join and earn rewards.")

#this is the function that checks if the user added contacts to the group and provides reward
def gainReward_command(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    # Checking if a user is in the group
    if user_id not in context.bot.get_chat_member(GROUP_CHAT_ID, user_id).user.id:
        context.bot.send_message(update.message.chat_id, 'You must first join our group')
    else:
        invited_users = update.message.new_chat_members
        for user in invited_users:
            context.bot.send_message(update.message.chat_id, f"Congratulations! You've earned a reward for inviting {user.first_name} to the group.")

if __name__ == '__main__':

    print('starting bot .......')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, gainReward_command))

    app.run_polling(poll_interval=3)
