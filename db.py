from tinydb import TinyDB, Query, where

db = TinyDB('db.json')

def mkitem(chat_id, item, owner):
    itemlist = db.table(str(chat_id))
    if not itemlist.search(where('name') == item):
        itemlist.insert({'name': item, 'owner': owner})
        return True
    return False

def rmitem(chat_id, item):
    itemlist = db.table(str(chat_id))
    return itemlist.remove(where('name') == item)

def chown(chat_id, item, newowner):
    itemlist = db.table(str(chat_id))
    return itemlist.update({'owner': newowner}, where('name') == item)

def status(chat_id, get_owner_name):
    itemlist = db.table(str(chat_id))
    owners = {}
    for item in itemlist.all():
        owner_id = item['owner']['id']
        if owner_id not in owners.keys():
            owners[owner_id] = item['owner']
    result = ""
    for owner in owners.values():
        result += get_owner_name(owner) + ":\n"
        Item = Query()
        for item in itemlist.search(Item.owner.id == owner['id']):
            result += "- " + item['name'] + "\n"
    return result;
