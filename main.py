from pathways.processes.pyrolysis import Pyrolysis
from core.pathway import Pathway

pyro = Pyrolysis(parameters={"biochar_yield": 0.3})

pathway = Pathway([pyro])

flows, emissions = pathway.run({
    "dry_wood": 1000
})

print(flows)
print(emissions)