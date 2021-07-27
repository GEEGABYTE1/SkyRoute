from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:

landmark_string = None
for letter, word in landmark_choices.items():
  string = ""
  string += str(letter) + " "
  string += str(word)
  landmark_string = string 

def greet():
  print('Hi there and welcome to SkyRoute!')
  print()
  print("We'll help you find the shortest route between the following Vancouver landmarks: {}".format(landmark_string))

def skyroute():
  greet()

def set_start_and_end(start_point, end_point):
  pass

def get_start():
  pass

def get_end():
  pass
