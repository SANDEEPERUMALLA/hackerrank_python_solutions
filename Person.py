class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        text = 'Name1: {name}, Age: {age}'.format(name=self.name, age=self.age)
        return text

    def __cmp__(self, other):
        if self.age < other.age:
            return -1
        elif self.age > other.age:
            return 1
        else:
            return 0


p1 = Person('John', 25)
p2 = Person('Smith', 30)
p3 = Person('Ramu', 18)
p_list = [p1, p2, p3]


def sorter(p):
    return p.name

p_list.sort(key=sorter)
for p in p_list:
    print(p)
