from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval




# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Graph:
    def __init__(self):
        self.rooms = {}
        self.length = 0

    def __str__(self):
        return f"Current rooms are {self.rooms}"

    def add_room_to_graph(self, room_id, exits):
        self.rooms[room_id] = {}
        for i in exits:
            room_copy = dict.copy(self.rooms[room_id])
            room_copy[i] = "?"
            self.rooms[room_id] = room_copy
        self.length += 1

    
    def update_rooms(self, room_id, direction, links_to):
        if direction == "n":
            opp = "s"
        elif direction == "s":
            opp = "n"
        elif direction == "w":
            opp = "e"
        elif direction == "e":
            opp = "w"
        room_copy = dict.copy(self.rooms[room_id])
        sec_room_copy = dict.copy(self.rooms[links_to])
        room_copy[direction] = links_to
        sec_room_copy[opp] = room_id
        self.rooms[links_to] = sec_room_copy
        self.rooms[room_id] = room_copy






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

visited = {}
traversal_graph = Graph()
current = player.current_room
stack = Stack()
queue = Queue()

print(room_graph)

# while len(visited_rooms) < len(room_graph):
#     current_room = player.current_room.id
#     room_exits = player.current_room.get_exits()
#     stack.push(room_exits)

#     #Check
#     if player.current_room.id not in visited_rooms:
#         # ?
#         # visited_rooms[player.current_room.id] = player.current_room.get_exits()
#         visited[player.current_room.id] = player.current_room.get_exits()
#         # for e in player.current_room.get_exits()

#     # print(f"While {room_exits}")
#     # push to stack then move 
#     while len(stack.stack) < 1:
#         print(stack.pop())

opposite_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


            
def mapTraversal(player, move=''):

    if len(visited) == len(room_graph):
        return


    current_room = player.current_room.id

    if player.current_room.id not in visited:
        visited[player.current_room.id] = {}
        for exit in player.current_room.get_exits():
            visited[player.current_room.id][exit] = '?'

    if move is not '':
        opposite = opposite_directions[move]
        last_Room = player.current_room.get_room_in_direction(opposite)
        visited[current_room][opposite] = last_Room.id

    new_move = '?'

    #  travel in that direction of unexplored path
    for exit_room in player.current_room.get_exits():
        if visited[current_room][exit_room] == '?':
            
            new_move = exit_room
            # move player 
            player.travel(exit_room)
            # Append the current exit to the traversal path for test
            traversal_path.append(exit_room)
            # Set the new room to the current room 
            new_room = player.current_room.id
            visited[current_room][exit_room] = new_room
            mapTraversal(player, exit_room)
            break

    # find the nearest unexplored exit
    path = []

    if new_move == '?':
        q = Queue()
        visited_rooms = set()
        q.enqueue([current_room])


        while q.size() > 0:
            path = q.dequeue()
            current_room = path[-1]

            if current_room not in visited_rooms:
                visited_rooms.add(current_room)

                # If the current room has an unexplored exit
                if '?' in visited[current_room].values():
                    path = path
                    q = Queue()
                    break

                # Add it to the path to search through and add it to the queue
                for neighbor in visited[current_room].values():
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
    
    for to_room in path:
        room = player.current_room.id
        graph = visited[room].keys()

        for v in graph:
            if visited[room][v] == to_room:
                player.travel(v)
                traversal_path.append(v)

    mapTraversal(player)


mapTraversal(player)

# def populate_graph():
#     # while True:
#     # for room_exit in player.current_room.get_exits():
#     traversal_graph.add_room_to_graph(current.id, current.get_exits())
#     stack.push(traversal_graph.rooms[current.id])
#     while stack.size() > 0:
#         e = stack.pop()
#         print(f"Pop {e}")
#         for room_exit in e:
#             print(f"loop {room_exit}")
#             print(f"visited {visited}")
#             # Room hasn't been traveled to 
#             if traversal_graph.rooms[current.id][room_exit] != "?":
#                 player.travel(room_exit)
#             player.travel(room_exit)
#             traversal_graph.add_room_to_graph(player.current_room.id, current.get_exits())
#             traversal_graph.update_rooms(current.id, room_exit, player.current_room.id)

    # if traversal_graph[current.id] not in visited:
    #     for room_exit in player.current_room.id:
    #         print(f"Exits {room_exit}")
    #         player.travel(room_exit)
    #         traversal_graph.add_room_to_graph(player.current_room.id, player.current_room.get_exits())
    #         print(f"Player {player.current_room.id}")
    #         print(f"Current {current.id}")
    #         traversal_graph.update_rooms(current.id, room_exit, player.current_room.id)
    #         # stack.push(room_exits.pop())
    #         print(f"Stack - {stack.pop()}")

# def get_unexplored()

# traversal_graph.add_room_to_graph(player.current_room.id, player.current_room.get_exits())
# traversal_graph.add_room_to_graph(3)
# traversal_graph.update_rooms(3, "n", 0)
print(f"My Graph {traversal_path}")
# populate_graph()
# my_queue = []


# player.current_room.get_exits()


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)



if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")




#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     print(f"Current room - {player.current_room.id}")
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
