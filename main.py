from modulea.example_funcs import add
from moduleb.subtract_func import subtract

def hello_world():
  print("hello world")

def run():
  hello_world()
  print("Loading from ./modulea/example_funcs.py", add(1, 2))
  print("Loading from ./moduleb/subtract_func.py", subtract(1, 2))

if __name__ == "__main__":
  run()