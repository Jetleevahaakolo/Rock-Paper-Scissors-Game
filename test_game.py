# Unit Testing
import pytest
import Module

def title(title):
    return print("Welcome to rock, paper, scissors!")

def test_title():
    assert title(title) == print("Welcome to rock, paper, scissors!")