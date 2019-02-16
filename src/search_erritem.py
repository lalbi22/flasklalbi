class ErrSearchItem:
    # text1 = []
    # strin = ""

    def __init__(self, text):
        self.text1 = text

    def get(self):
        strin = ""
        for test in self.text1:
            if strin == "":
                strin += str(test)
            else: strin += ", " + str(test)
        return strin

    def set(self, strin):
        self.text1.append(str(strin))


text1 = ["index", "element"]
obj = ErrSearchItem(text1)
obj.set("tag")
print(text1)
print(obj.get())
