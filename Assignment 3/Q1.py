import copy

def print_rows(list):
    for i in list:   
        print(i)
    print("\n")


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.heuristic = -1

    @staticmethod
    def calculate_coordinates(value, init, goal):
        x_init, y_init, x_goal, y_goal = 0,0,0,0
        for j in range(0,3):
            for i in range(0,3):
                if init.data[j][i] == value:
                    x_init = i; y_init = j
                if goal[j][i] == value:
                    x_goal = i; y_goal = j

        return x_init, y_init, x_goal, y_goal

    @staticmethod
    def calculate_euclidean(init, goal):
        net_heuristic = 0
        for i in range (1,9):
            x_init, y_init, x_goal, y_goal = Node.calculate_coordinates(i, init, goal)
            net_heuristic += ((x_init - x_goal)**2 + (y_init - y_goal)**2)**0.5
        return net_heuristic

    @staticmethod
    def calculate_manhattan(init, goal):
        net_heuristic = 0
        for i in range (1,9):
            x_init, y_init, x_goal, y_goal = Node.calculate_coordinates(i, init, goal)
            net_heuristic += abs(x_init - x_goal) + abs(y_init - y_goal)
        return net_heuristic

    @staticmethod
    def calculate_minkowski(init, goal, p):
        net_heuristic = 0
        for i in range (1,9):
            x_init, y_init, x_goal, y_goal = Node.calculate_coordinates(i, init, goal)
            net_heuristic += (abs((x_init - x_goal)**p) + abs((y_init - y_goal)**p))**(1/p)
        return net_heuristic


initial_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

init = Node(initial_state, [0])

print("Initial State- \n")
print_rows(initial_state)
print("Goal State- \n")
print_rows(goal_state)

print("Euclidean Heuristic Value between these states- ", end='')
print(Node.calculate_euclidean(init, goal_state))

print("Manhattan Heuristic Value between these states- ", end='')
print(Node.calculate_manhattan(init, goal_state))

print("Minkowski Heuristic Value between these states- ", end='')
print(Node.calculate_minkowski(init, goal_state, p=2))
