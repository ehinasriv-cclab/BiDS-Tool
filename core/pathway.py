class Pathway:
    def __init__(self, processes):
        self.processes = processes

    def run(self, initial_inputs):
        flows = initial_inputs.copy()
        emissions_total = {}

        for process in self.processes:
            result = process.run(flows)

            # update flows
            flows.update(result.get("outputs", {}))

            # aggregate emissions
            for k, v in result.get("emissions", {}).items():
                emissions_total[k] = emissions_total.get(k, 0) + v

        return flows, emissions_total