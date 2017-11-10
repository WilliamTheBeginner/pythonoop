class Outcome:
    set1 = []

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds
        set1.insert(self)
    def __eq__(self, other):
        return self.name == other.name and self.odds == other.odds
    def __hash__(self):
        return hash((self.name, self.odds))
oc1 = Outcome('Red', 1)
oc2 = Outcome('Red', 1)
oc3 = Outcome('Black', 1)
oc4 = Outcome('1', 35)
oc5 = Outcome('1', 11)
# hash is the same for both objects
print(hash(oc1))
print(hash(oc2))
# both objects are equal
print(oc1 == oc2)

if oc1.name == oc2.name:
    print(True)
else:
    print(False)
