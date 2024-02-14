import secrets
from datetime import datetime




class Tokens:
    # tokens = {token: timestamp, token: timestamp, ...}
    def __init__(self, tokens = {}):
        self.tokens = tokens

    def add_token(self):
        new_token = secrets.token_hex(4)
        self.tokens[new_token] = datetime.timestamp(datetime.now()) + 10
        print(f"Token toegevoegd: {self.tokens[new_token]}")
        return new_token

    def dict_tokens(self):
        return self.tokens
    
    def check_token(self, token):
        return token in self.tokens
    
    def check_time(self, token):
        print(f"Token: {token}, tijd: {self.tokens[token]}")
        return self.tokens[token] > datetime.timestamp(datetime.now())