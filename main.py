import yaml
from riverflow.engine import Engine

def load_config(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    config = load_config('riverflow/config.yaml')
    engine = Engine(config)
    engine.execute()
