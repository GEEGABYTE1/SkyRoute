from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices
import time

# Build your program below:

landmark_string = ""
stations_under_construction = []

for letter, place in landmark_choices.items():
  landmark_string += "{letter} ---> {place} \n".format(letter=letter, place=place)

def greet():
  print("Hi there and welcome to SkyRoute! ")
  print("We'll help you find the shortest route between the following Vancouver landmarks {}".format(landmark_string))

def skyroute():
  greet()
  new_route()
  goodbye()

def set_start_and_end(start_point, end_point):
  if start_point != None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    
    if change_point == 'b':
      start_point = get_start()
      end_point = get_end()
    elif change_point == 'o':
      start_point = get_start()
    elif change_point == 'd':
      end_point = get_end()
    else:
      print('That command is not valid')
      return set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()

  return start_point, end_point

def get_start():
  start_point_letter = input('Where are you coming from? Type in the corresponding letter: ')
  retrieve_letter = landmark_choices.get(start_point_letter, None)
  if retrieve_letter:
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("We do not have any data on that landmark")
    return get_start()
def get_end():
  end_point_letter = input('Where are you headed? Type in the corresponding letter: ') 
  retrieve_letter = landmark_choices.get(end_point_letter, None)
  if retrieve_letter:
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
     print("We do not have any data on that landmark")
     return get_end()

def new_route(start_point=None, end_point=None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  shortest_route_string = ""
  for i in shortest_route:
    shortest_route_string += "{} ----> ".format(i)
  shortest_route_string = shortest_route_string.strip("----> ")
  print("The shortest route from {start} to {end} is {path}".format(start=start_point, end=end_point, path=shortest_route_string))
  again = input("Would you like to see another route? Enter y/n: ")
  if again == 'y':
    show_landmarks()
    new_route(start_point, end_point)
  
def show_landmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == 'y':
    print(landmark_string)



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

def goodbye():
  print("Thanks for using SkyRoute!")



#print(get_route('Stanley Park', 'Science World'))
print(skyroute())