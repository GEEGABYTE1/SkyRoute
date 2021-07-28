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

stations_under_construction = ['My face', 'Mangoes']

def greet():
  print('Hi there and welcome to SkyRoute!')
  print()
  print("We'll help you find the shortest route between the following Vancouver landmarks: {}".format(landmark_string))

def skyroute():
  greet()
  new_route()
  goodbye()

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
  shortest_route = get_route(start_point, end_point)
  if shortest_route:
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {a} to {b} is: {}".format(shortest_route_string, a=start_point, b=end_point))
  else:
    print('Unfortunately, there is currently no path between {a} and {b} due to maintenance.'.format(a=start_point, b=end_point))
  time.sleep(0.1)
  print()
  again = input('Would you like to see another route? Enter y/n: ')
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
      metro_system = get_active_stations() if stations_under_construction else vc_metro 
      if len(stations_under_construction) != 0:
          possible_route = dfs(metro_system, start_station, end_station)
          if possible_route == None:
              return None 

    
        
      route = bfs(metro_system, start_station, end_station)
      
      if route:
        routes.append(route)
  
  shortest_route = min(routes, key=len)
  return shortest_route

def goodbye():
    print("Thanks for using SkyRoute!")

def get_active_stations():
    updated_metro = vc_metro 
    for station_under_construction in stations_under_construction:
        for current_station in vc_metro[station_under_construction]:
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(station_under_construction)
            else:
                updated_metro[current_station] = set([])
    
    return updated_metro



print(skyroute())
  
