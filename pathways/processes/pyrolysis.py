from core.process import Process
from core.material import Material

class Pyrolysis(Process):
    def run(self, inputs):
        wood = inputs["woody_biomass"]

        carbon = wood.amount * (1 - wood.get("moisture_content")) * wood.get("carbon_fraction")

        biochar_yield = self.parameters.get("biochar_yield", 0.3)

        biochar = Material(
            "biochar",
            wood.amount * biochar_yield,
            properties={
                "carbon_fraction": 0.75
            }
        )

        return {
            "outputs": {"biochar": biochar},
            "emissions": {
                "CO2": carbon * 0.5
            }
        }