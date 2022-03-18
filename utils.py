def mkitem(itemlist, item, owner):
    if item not in itemlist.keys():
        itemlist[item] = owner
        return True
    return False

def rmitem(itemlist, item):
    if item in itemlist.keys():
        del itemlist[item]
        return True
    return False

def chown(itemlist, item, newowner):
    if item in itemlist.keys():
        itemlist[item] = newowner
        return True
    return False

def status(itemlist, get_owner_name):
    owners = _get_owners(itemlist)
    result = ""
    for owner in owners.keys():
        result += get_owner_name(owner) + ":\n"
        for item in owners[owner]:
            result += "- " + str(item) + "\n"
    return result;

def _get_owners(itemlist):
    owners = {}
    for itemname in itemlist.keys():
        owner = itemlist[itemname]
        if owner not in owners:
            owners[owner] = []
        owners[owner].append(itemname)
    return owners
