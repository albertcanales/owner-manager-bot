from telegram import ParseMode
from telegram.ext import Updater, CommandHandler
import db

def start(update, context):
    message = """
Hi! I help you keep track of the ownership of items in this group.
Type /help to see my available commands.
Created by Albert Canales [albertcanales.com]
    """
    send_message(update, context, message)

def help(update, context):
    message = """
I'm very simple! Here's my commands:
- /help: I show you my available commands (recursion!)
- /mkitem `item`: I create new items with the creator as the owner
- /rmitem `item`: I remove the given items
- /chown `item`: I change the ownership of item to you
- /status: I display the owner of each item
    """
    send_message(update, context, message)

def mkitem(update, context):
    params = get_parameters(update, context)
    if params:
        owner = user_serializable(update.message.from_user)
        if db.mkitem(update.message.chat_id, params[0], owner):
            send_message(update, context, "ℹ️ Item created successfully")
        else:
            send_message(update, context, "🚫 Item already exists")
    else:
        send_parameters_error(update, context);


def rmitem(update, context):
    params = get_parameters(update, context)
    if params:
        owner = user_serializable(update.message.from_user)
        if db.rmitem(update.message.chat_id, params[0]):
            send_message(update, context, "ℹ️ Item removed successfully")
        else:
            send_message(update, context, "🚫 Item does not exists")
    else:
        send_parameters_error(update, context);

def chown(update, context):
    params = get_parameters(update, context)
    if params:
        owner = user_serializable(update.message.from_user)
        if db.chown(update.message.chat_id, params[0], owner):
            send_message(update, context, "ℹ️ Changed ownership successfully")
        else:
            send_message(update, context, "🚫 Item does not exists")
    else:
        send_parameters_error(update, context);

def status(update, context):
    message = db.status(update.message.chat_id, get_user_name)
    if message:
        send_message(update, context, message)
    else:
        send_message(update, context, "ℹ️ There are no items")

def user_serializable(user):
    result = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name
    }
    return result

def get_user_name(user):
    result = user['first_name']
    if user['last_name']:
        result += " " + user['last_name']
    return result

def send_parameters_error(update, context):
    message = """
    🚫 Insuficient parameters. Check /help for usages for each command.
    """
    send_message(update, context, message)

def send_message(update, context, message):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message,
        parse_mode=ParseMode.MARKDOWN)


def get_parameters(update, context):
    return update.message.text.split(' ', 1)[1:]

def main():

    print("Starting bot...")

    TOKEN = open('token.txt').read().strip()
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('mkitem', mkitem))
    dispatcher.add_handler(CommandHandler('rmitem', rmitem))
    dispatcher.add_handler(CommandHandler('chown', chown))
    dispatcher.add_handler(CommandHandler('status', status))
    updater.start_polling()

    print("Bot started")


main()
