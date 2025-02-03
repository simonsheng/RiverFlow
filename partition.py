from riverflow.adaptor import Adaptor
from riverflow.filter import Filter
from riverflow.transformer import Transformer
from riverflow.partition import Partition

class Engine:
    def __init__(self, config):
        self.config = config
        self.adaptor = Adaptor(config['adaptor']['input_path'], config['adaptor']['output_path'])
        self.filter = Filter(config['filter']['criteria'])
        self.transformer = Transformer(config['transformer']['operation'], config['transformer'].get('factor'))
        self.partition = Partition(config['partition']['num_threads'])

    def execute(self):
        data = self.adaptor.read_data()
        data = self.filter.apply(data)
        data = self.transformer.apply(data)
        self.partition.process(data, self.adaptor.write_data)
