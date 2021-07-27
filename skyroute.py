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
  print()
  start_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")

  start_point_checker = landmark_choices.get(start_point_letter, None)

  if start_point_checker != None:
    end_point = landmark_choices[start_point_letter]
    return end_point
  else:
    print('We do not have any data about that very landmark')
    return get_end()

def new_route(start_point=None, end_point=None):
  start_point, end_point = set_start_and_end(start_point, end_point)

def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []

  for start_station in start_stations:
    for end_station in end_stations:
      route = bfs(vc_metro, start_station, end_station)
      
      if route:
        routes.append(route)
  
  shortest_route = min(routes, key=len)
  return shortest_route


  

first = None 
second = None
for name in vc_landmarks.keys():
    first = name 
    break 

counter = 0 
for name in vc_landmarks.keys():
    counter += 1
    if counter == 2:
        second = name 
        break
    continue  


print(get_route(first, second))
