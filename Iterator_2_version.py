class ProgrammingLanguages:

    _name = ("Python", "Golang", "C#", "C", "C++", "Java", "SQL", "JS")

    def __init__(self, first=None):
        self.index = (-1 if first is None else
                      ProgrammingLanguages._name.index(first) - 1)

    def __call__(self):
        self.index += 1
        if self.index < len(ProgrammingLanguages._name):
            return ProgrammingLanguages._name[self.index]
        raise StopIteration

#From C# to last
for lang in iter(ProgrammingLanguages("C#"), None):
    print(lang, end=" ")



#From 1st to C
# pl = ProgrammingLanguages()
# for lang in iter(pl, "C"):
#     print(lang, end=" ")