class Material:
    def __init__(self, name, amount, unit="kg", properties=None):
        self.name = name
        self.amount = amount
        self.unit = unit
        self.properties = properties or {}

    def get(self, prop, default=None):
        return self.properties.get(prop, default)

    def set(self, prop, value):
        self.properties[prop] = value

    def copy(self):
        return Material(
            self.name,
            self.amount,
            self.unit,
            self.properties.copy()
        )

    def __repr__(self):
        return f"{self.name}: {self.amount} {self.unit} | {self.properties}"