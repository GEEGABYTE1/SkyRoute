from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices
import time

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
  if start_point != None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")

    if change_point == "b":
      start_point = get_start()
      end_point = get_end()
    elif change_point == "o":
      start_point = get_start()
    elif change_point == "d":
      end_point = get_end()
    else:
      print("The command does not seem to be valid.")
      return set_start_and_end(start_point, end_point)

  else:
    start_point = get_start()
    end_point = get_end()
  
  return start_point, end_point
def get_start():
  print()
  for letter, destination in landmark_choices.items():
    print("Here are your choices: ")
    time.sleep(0.2)
    print(letter + ' = ' + destination)
  print()
  time.sleep(0.2)
  start_point_letter = input("Where are you coming from? Please type in the corresponding letter: ")

  start_point_checker = landmark_choices.get(start_point_letter, None)

  if start_point_checker != None:
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print('We do not have any data about that very landmark')
    return get_start()

def get_end():
  pass


print(get_start())