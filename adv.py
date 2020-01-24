from room import Room
from player import Player
from world import World
from queue import Queue

import random
from ast import literal_eval


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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

print(room_graph)

while len(visited_rooms) < len(room_graph):
    current_room = player.current_room.id
    room_exits = player.current_room.get_exits()
    stack.push(room_exits)

    #Check
    if player.current_room.id not in visited_rooms:
        # ?
        # visited_rooms[player.current_room.id] = player.current_room.get_exits()
        visited[player.current_room.id] = player.current_room.get_exits()
        # for e in player.current_room.get_exits()

    # print(f"While {room_exits}")
    # push to stack then move 
    while len(stack.stack) < 1:
        print(stack.pop())



# for room_exit in player.current_room.get_exits():
#     traversal_graph.add_room_to_graph(current.id, current.get_exits())
#     print(f"Exits {room_exit}")
#     player.travel(room_exit)
#     traversal_graph.add_room_to_graph(player.current_room.id, player.current_room.get_exits())
#     print(f"Player {player.current_room.id}")
#     print(f"Current {current.id}")
#     traversal_graph.update_rooms(current.id, room_exit, player.current_room.id)
#     # stack.push(room_exits.pop())
    # print(f"Stack - {stack}")


# traversal_graph.add_room_to_graph(player.current_room.id, player.current_room.get_exits())
# traversal_graph.add_room_to_graph(3)
# traversal_graph.update_rooms(3, "n", 0)
# print(f"My Graph {traversal_graph}")
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
player.current_room.print_room_description(player)
while True:
    print(f"Current room - {player.current_room.id}")
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
