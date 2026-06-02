from pathlib import Path


class Extract:
    def __init__(self, config):
        self.config = config
        
    def extract_data(self):
        path = self.config.path
        with open(path, 'r') as file:
            data = file.read()
        return data

