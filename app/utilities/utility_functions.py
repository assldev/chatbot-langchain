import json
from utilities.constants import Errors
      
def load_json(json_file_path: str):
    try:
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
            return json_data
    except FileNotFoundError as e:
        print(f"{Errors.FILE_NOT_FOUND}: {json_file_path}")
        raise(e)
    except json.JSONDecodeError as e:
        print(f"{Errors.JSON_DECODE_ERROR}: {json_file_path}")
        raise(e)

def load_txt(txt_file_path: str):
    ...

def convert_pdf_to_txt(pdf_file_path: str, txt_file_path: str):
    ...