class Outcome:

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash((self.name, self.odds))

    def winAmount(self, amount):
        return self.odds * self.amount

    def __str__(self):
        return 'Outcome: {}({}:1)'.format(self.name, self.odds)

    def __repr__(self):
        return 'Outcome({}, {}) {}'.format(self.name, self.odds, self.__hash__())
