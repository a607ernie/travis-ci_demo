import sys
sys.path.append('.')
import hello

def test_says_world():
    assert hello.say_what() == 'world'