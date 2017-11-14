from typing import List


class MyClass:

    kind = 12345  # shared by all instance

    def __init__(self, i):
        """Constructor"""
        self.i = i
        self.tricks = []

    def add_tricks(self, tricks: List[str]) -> None:
        self.tricks.extend(tricks)

    def print_greeting(self) -> str:
        """Print a greeting"""
        return f'hello world {self.i}'

    def add_trick(self, trick: str):
        """Add a trick to the list of tricks"""
        self.tricks.append(trick)
