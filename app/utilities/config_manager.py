import os
from utilities.constants import Errors
from utilities.utility_functions import load_json

class ConfigManager:
  
  config = None

  def __init__(self, config_file_path: str):
    self.config = load_json(config_file_path)

  def get_value(self, key: str):
    if self.config:
      try:
        return self.config[key]
      except KeyError as e:
        value = os.environ.get(key)
        if value:
          return value
    
    raise Exception(f"{Errors.CONFIG_KEY_NOT_FOUND}: {key}")