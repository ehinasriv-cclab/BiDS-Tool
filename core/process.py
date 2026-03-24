from core.flow import Flow

class Process:
    def __init__(self, name=None, parameters=None):
        self.name = name or self.__class__.__name__
        self.parameters = parameters or {}

    def run(self, inputs):
        inputs: dict[str, Flow]
        returns = {
            "outputs": dict[str, Flow],
            "emissions": dict[str, float],
}
        
        raise NotImplementedError("Each process must implement the run() method")