class TodoList(object):

    def __init__(self, title=None):
        self.title = title
        self.items = list()

    def print_list(self, tdl=None):
        if tdl is None:
            tdl = range(len(self.items))

        for i in tdl:
            item = "{0}. {1}".format(i, self.items[i])
            print(item)

    def __str__(self, tdl=None):
        return str(self.title)

    def __len__(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    def __setitem__(self, key, update):
        self.items[key] = update

    def __delitem__(self, key):
        del self.items[key]

    def search(self, query):
        return [i for i, item in enumerate(self.items) if query in item]

if __name__ == "__main__":
    x = TodoList("Shopping list")
    print(str(x))
    x.add("buy salad")
    x[0] = "buy potato"
    x.add("buy tomato")
    del x[1]
    x.print_list(x.search("potato"))
    
