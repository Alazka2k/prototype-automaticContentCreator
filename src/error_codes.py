import json
import os

class ErrorCode:
    def __init__(self):
        json_path = os.path.join(os.path.dirname(__file__), 'error_codes.json')
        with open(json_path, 'r') as f:
            self.error_codes = json.load(f)
        for code, data in self.error_codes.items():
            setattr(self, data['code'], int(code))

ErrorCode = ErrorCode()

def get_error_message(code):
    return ErrorCode.error_codes[str(code)]['message']

def get_error_code_name(code):
    return ErrorCode.error_codes[str(code)]['code']