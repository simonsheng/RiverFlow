from riverflow.adaptor import FileAdaptor, FTPAdaptor, MySQLAdaptor, CosmosDBAdaptor
from riverflow.filter import Filter
from riverflow.transformer import Transformer
from riverflow.partition import Partition

class Engine:
    def __init__(self, config):
        self.config = config
        adaptor_config = config['adaptor']
        if adaptor_config['type'] == 'File':
            self.adaptor = FileAdaptor(adaptor_config['input_path'], 'r')
        elif adaptor_config['type'] == 'FTP':
            self.adaptor = FTPAdaptor(adaptor_config['host'], adaptor_config['username'],
                                      adaptor_config['password'], adaptor_config['input_path'], 'r')
        elif adaptor_config['type'] == 'MySQL':
            self.adaptor = MySQLAdaptor(adaptor_config['host'], adaptor_config['user'],
                                        adaptor_config['password'], adaptor_config['database'],
                                        adaptor_config['query'], 'r')
        elif adaptor_config['type'] == 'CosmosDB':
            self.adaptor = CosmosDBAdaptor(adaptor_config['endpoint'], adaptor_config['key'],
                                           adaptor_config['database'], adaptor_config['container'],
                                           adaptor_config['query'], 'r')

        self.filter = Filter(config['filter']['criteria'])
        self.transformer = Transformer(config['transformer']['operation'], config['transformer'].get('factor'))
        self.partition = Partition(config['partition']['num_threads'])

    def execute(self):
        data = self.adaptor.read_data()
        data = self.filter.apply(data)
        data = self.transformer.apply(data)
        self.partition.process(data, self.adaptor.write_data)
