from core import Pathway
from pathways.feedstock.biomass import create_woody_biomass
from pathways.processes.pyrolysis import Pyrolysis

# 1. Create feedstock
biomass = create_woody_biomass(1000)

# 2. Create processes
pyrolysis = Pyrolysis(parameters={
    "biochar_yield": 0.3
})

# 3. Build pathway
pathway = Pathway([
    pyrolysis
])

# 4. Run pathway
flows, emissions = pathway.run({
    "woody_biomass": biomass
})

# 5. View results
print("Final flows:", flows)
print("Emissions:", emissions)