class Flow:
    def __init__(self, name, amount, unit="kg", properties=None):
        self.name = name
        self.amount = amount
        self.unit = unit
        self.properties = properties or {}

    def __repr__(self):
        return f"{self.name}: {self.amount} {self.unit}"