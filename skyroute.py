from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices
import time
routes_global = []



landmark_string = ""
stations_under_construction = []
starter_point_letter = None


for letter, place in landmark_choices.items():
  landmark_string += "{letter} ---> {place} \n".format(letter=letter, place=place)

def greet():
  print("Hi there and welcome to SkyRoute! ")
  print("We'll help you find the shortest route between the following Vancouver landmarks {}\n".format(landmark_string))

def skyroute():
  greet()
  playing = True
  
  while playing:
    time.sleep(0.2)
    print()
    running = new_route()
    if running == False:
      break
    elif running == '/add_construction':
      print(add_construction())
    else:
      continue
    
    
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
  start_point_letter = start_point_letter
  retrieve_letter = landmark_choices.get(start_point_letter, None)
  if retrieve_letter:
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("We do not have any data on that landmark")
    return get_start()

def get_end():
  end_point_letter = input('Where are you headed? Type in the corresponding letter: ') 
  if end_point_letter == starter_point_letter:
    print("You are already at your destination")
    return new_route()
  else:
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

  if shortest_route == None:
    print("No optimal path found")
    return 
  
  shortest_route_string = ""
  for i in shortest_route:
    shortest_route_string += "{} ----> ".format(i)
  shortest_route_string = shortest_route_string.strip("----> ")
  if shortest_route_string != "":
    print("The shortest route from {start} to {end} is {path}".format(start=start_point, end=end_point, path=shortest_route_string))
    time.sleep(0.1)
    question = input("Would you like to see another path of the same two landmarks? Enter y/n: ")
    if question == 'y':
      try:
        shortest_route_output = routes_global.pop()
        shortest_route_string = ""
        for i in shortest_route_output:
          shortest_route_string += "{} ----> ".format(i)
        shortest_route_string = shortest_route_string.strip("----> ")
        print(shortest_route_string)
        print()
      except IndexError:
        print('There is no other possible path!')
    else:
      pass
        

  else:
    print("There is currently no path between {start} and {end}".format(start=start_point, end=end_point))
  again = input("Would you like to see another route? Enter y/n: ")
  if again == 'y':
    show_landmarks()
    new_route(start_point, end_point)
  
  elif again == 'n':
    return False
  elif again == '/add_construction':
    return '/add_construction'
  
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

      if len(stations_under_construction) != 0:
        metro_system = get_active_stations()
        possible_route = dfs(metro_system, start_station, end_station)
        if possible_route == None:
          return None
        else:
          return possible_route
      else:
        metro_system = vc_metro

      route = bfs(metro_system, start_station, end_station)

      if route:
        routes.append(route)
  
  shortest_route = min(routes, key=len)
  routes_global += routes
  return shortest_route

def get_active_stations():
  updated_metro = vc_metro
  for station_under_construction in stations_under_construction:
    for current_station in vc_metro[station_under_construction]:
      if current_station != station_under_construction:
        updated_metro[current_station]  -= set(stations_under_construction)
      else:
        updated_metro[current_station] = set([])
  
  return updated_metro

def add_construction():
  stations = []
  print("Here are the stations that can be under construction: ")
  for list in vc_landmarks.values():
    for station in list:
      if not station in stations:
        stations.append(station)
  
  for station in stations:
    print(station)
  print()
  
  station = input('Please type in a name of a station: ')
  if station in stations_under_construction:
    print('That station is already under construction')
    add_construction()
  elif not station in stations:
    print('That station does not seem to be recorded')
  else:
    stations_under_construction.append(station)


def goodbye():
  print("Thanks for using SkyRoute!")



print(skyroute())
