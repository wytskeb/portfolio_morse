import secrets

class Tokens:

    def __init__(self, tokens = []):
        self.tokens = tokens

    def add_token(self):
        new_token = secrets.token_hex(4)
        self.tokens.append(new_token)
        return new_token

    def list_tokens(self):
        return self.tokens
    
    def check_token(self, token):
        return token in self.tokens