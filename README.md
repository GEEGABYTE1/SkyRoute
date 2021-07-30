# SkyRoute 🌃🛩
A simulated GPS System 🗺

With the use of both Breadth-First and Depth-First Graph Search algorithms, users can view which stations in simulated real-time will take them to their desired landmark in Vancouver. 



# Controls 
 
 To choose specific landmarks as a starting point and as a destination, the user will have to type a corresponding letter from *a-z* that matches with their desired landmarks. The program will output which letters match with which landmark as a string. 

 - `y`= When the program prompts, `Would you like to see the list of landmarks again?`, `y` represents *yes* and the program will recursively called `new_route()`.
 - `n`= When the program prompts, `Would you like to see the list of landmarks again?`, `n` represents *no* and the program will not output another path, and will end the program.
 - `/add_construction` = While the program prompts `Would you like to see the list of landmarks again`, users can type `/add_construction` to add a specific station under construction. When a station is under construction, all landmarks that have that very station as a one of the travel paths will be deleted. This may modify the path between a start point and an end point.
 - `b`: When the user wants to see a new path, the program will prompt, `What you would like to change?`. If the user types `b`, this indicates to the program that the user wants to change the initial start point and their destination.
 - `o`: When the user faces, `What you would like to change?`, when trying to find a new path, `o` indicates to the program that the user wants to change their starting point.
 - `d`: Works just like `o` and `b`, however, `d` will allow the user to change their destination.

# Depth-First Implementation

The Depth-First algorithm is used to see if there is a station that correponds to a landmark. Since we users can add stations under construction with `/add_construction`, it would not make any sense for the station to still be running. Hence, to make the program flow with those changes, if there is a station that is under construction, we will use the depth-first algorithm to see if there is another path from the start to the destination. If there is, we will return the possible route as a path, otherwise, we will return that there is no path possible. We return this because each landmark has at least one station. When there is a station under construction, we remove the station from each landmark. Therefore, there may be possibility where there actually is no path between a start point and the desired destination.

# Breadth-First Implementation
The BFS algorithm is used when there is no station under construction. Since the algorithm will append a list of each possible path (which is also an array), we want to return the shortest, as that will return the shortest path (this was done using Merge Sort). However, just like DFS, if there is no possible route between them, then the algorithm will return `None`, which will indicate to the user that there was no optimal path found. 

# More Information 
 
 ## Time Complexities:
 - Breadth-First: `O(no.vertices + no.edges)`
 - Depth-First: `O(no.vertices + no.edges)`
 - Merge-Sort: `O(n log n)`

To create a new route, the program takes the same start point and end point and calls various functions recursively under the same parameters.

Made in Python 🐍
 

