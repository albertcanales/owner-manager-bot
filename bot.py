def mkitem(itemlist, item, owner):
    if item not in itemlist.keys():
        itemlist[item] = owner

def rmitem(itemlist, item):
    if item in itemlist.keys():
        del itemlist[item]

def chown(itemlist, item, newowner):
    if item in itemlist.keys():
        itemlist[item] = newowner

def status(itemlist):
    owners = get_owners(itemlist)
    result = ""
    for owner in owners.keys():
        result += owner + ":\n"
        for item in owners[owner]:
            result += " - " + item + "\n"
    return result;

def get_owners(itemlist):
    owners = {}
    for itemname in itemlist.keys():
        owner = itemlist[itemname]
        if owner not in owners:
            owners[owner] = []
        owners[owner].append(itemname)
    return owners

def show_error(error):
    print(error)

def main():
    itemlist = {}
    mkitem(itemlist, "Silla", "Pablo")
    mkitem(itemlist, "Lápiz", "Sandra")
    mkitem(itemlist, "Comida", "Abel")
    print(status(itemlist))
    chown(itemlist, "Comida", "Sandra")
    print(status(itemlist))
    rmitem(itemlist, "Silla")
    print(status(itemlist))


main()