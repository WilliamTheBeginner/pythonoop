class Outcome:

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __eq__(self, other):
        return self.name == other.name and self.oods == other.odds

    def __ne__(self, other):
        return self.name != other.name and self.oods != other.odds

    def __hash__(self):
        return hash((self.name, self.odds))

    def winAmount(self, amount):
        self.odds * self.amount

    def __str__(self):
        pass

    def __repr__(self):
        pass
    
oc1 = Outcome('1', )
