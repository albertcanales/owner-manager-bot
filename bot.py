from telegram import ParseMode
from telegram.ext import Updater, CommandHandler
import utils

itemlists = {}

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
        owner = update.message.from_user
        itemlist = get_itemlist(update.message.chat_id)
        if utils.mkitem(itemlist, params[0], owner):
            send_message(update, context, "Item created successfully")
        else:
            send_message(update, context, "Item already exists")
    else:
        send_parameters_error(update, context);


def rmitem(update, context):
    params = get_parameters(update, context)
    if params:
        owner = update.message.from_user
        itemlist = get_itemlist(update.message.chat_id)
        if utils.rmitem(itemlist, params[0]):
            send_message(update, context, "ℹ️ Item removed successfully")
        else:
            send_message(update, context, "🚫 Item does not exists")
    else:
        send_parameters_error(update, context);

def chown(update, context):
    params = get_parameters(update, context)
    if params:
        owner = update.message.from_user
        itemlist = get_itemlist(update.message.chat_id)
        if utils.chown(itemlist, params[0], owner):
            send_message(update, context, "ℹ️ Changed ownership successfully")
        else:
            send_message(update, context, "🚫 Item does not exists")
    else:
        send_parameters_error(update, context);

def status(update, context):
    itemlist = get_itemlist(update.message.chat_id)
    message = utils.status(itemlist, get_user_name)
    if message:
        send_message(update, context, message)
    else:
        send_message(update, context, "ℹ️ There are no items")

def get_itemlist(chat_id):
    if chat_id not in itemlists.keys():
        itemlists[chat_id] = {}
    return itemlists[chat_id]

def get_user_name(user):
    result = user.first_name
    if user.last_name:
        result += " " + user.last_name
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
