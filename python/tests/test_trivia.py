import trivia
import pytest

class StubLogger:
    def __init__(self):
        self.logs = []
        
    def log(self, message):
        self.logs.append(message)

def test_deterministic():
    assert trivia.run(StubLogger()).logs == open("./result.txt", "r").read().split("\n")