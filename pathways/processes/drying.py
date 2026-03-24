from core.process import Process

class Drying(Process):
    def run(self, inputs):
        wood = inputs["woody_biomass"].copy()

        target_mc = self.parameters.get("target_moisture", 0.1)

        initial_mc = wood.get("moisture_content")

        # adjust mass (remove water)
        dry_mass = wood.amount * (1 - initial_mc)
        new_total_mass = dry_mass / (1 - target_mc)

        water_removed = wood.amount - new_total_mass

        wood.amount = new_total_mass
        wood.set("moisture_content", target_mc)

        return {
            "outputs": {"woody_biomass": wood},
            "emissions": {
                "water_evaporated": water_removed
            }
        }
    
    