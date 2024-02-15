#!/usr/bin/env python3

"""
tokens.py

This module contains the Tokens class and the global variable my_tokens
"""
import random
import string
from datetime import datetime

class Tokens:
    """
    This class is responsible for the creation and checking of API tokens
    """
    def __init__(self, tokens=None):
        if tokens is None:
            tokens = {}
        self.tokens = tokens

    def add_token(self):
        """
        This function adds a new token to the tokens dictionary.

        Returns:
            str: the new token
        """
        new_token = self._generate_token()
        self.tokens[new_token] = datetime.timestamp(datetime.now()) + 5
        print(f"Token toegevoegd: {self.tokens[new_token]}")
        return new_token

    def dict_tokens(self):
        """
        Returns the dictionary with all the tokens
        """
        return self.tokens

    def check_token(self, token):
        """
        Check if the given token is in the tokens dictionary.
        """
        return token in self.tokens

    def check_time(self, token):
        """
        Check if the given token is in the tokens dictionary.

        Returns:
            bool: True if token is valid, False if token is expired
        """
        print(f"Token: {token}, tijd: {self.tokens[token]}")
        return self.tokens[token] > datetime.timestamp(datetime.now()) - 10

    def cleanup_tokens(self):
        """
        Remove the given token from the tokens dictionary
        """
        t = self.tokens.copy()
        for token in t:
            if t[token] < datetime.timestamp(datetime.now()):
                self.tokens.pop(token)
                print(f"Verwijderd token: {token}")

    @staticmethod
    def _generate_token(length=8):
        """
        Generate a random token.

        Parameters:
            length (int): The length of the token.

        Returns:
            str: The randomly generated token.
        """
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    