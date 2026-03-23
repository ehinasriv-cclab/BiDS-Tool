from core.process import Process

class Pyrolysis(Process):
    def run(self, inputs):
        wood = inputs.get("dry_wood", 0)

        biochar = wood * self.parameters.get("biochar_yield", 0.3)

        return {
            "outputs": {
                "biochar": biochar
            },
            "emissions": {
                "CO2": wood * 0.2
            }
        }