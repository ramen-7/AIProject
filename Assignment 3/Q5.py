import copy

initial_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
finalout = []
visitedout = []
visited_set = set()
return_list = []

def calculate_misplaced(init, goal):
    cost = 0
    for i in range(0, 3):
        for j in range(0, 3):
            #print(i, j)
            if(goal[i][j] != init[i][j] and goal[i][j] != -1):
                cost+=1
                
    print (cost)
    return cost


def print_rows(list):
    for i in list:
        for j in i:
            print(j)
        print("\n")

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.parentweight = 0

    @staticmethod
    def not_in(self, visited):
        for node in visited:
            if (self.data == node.data):
                return 0
        return 1

    def find_miss(self):
        list = []
        for i in range(0, 3):
            for j in range(0, 3):
                #print(i,j)
                if (self.data[i][j] == 0):
                    #print("i=",i, "j=",j)
                    list.append(i) 
                    list.append(j)
                    break
                
            
        #print(list)
        return list

    def move_right(self, miss_y, miss_x):

        temp_arr=copy.deepcopy(self.data)
        temp = temp_arr[miss_y][miss_x]
        temp_arr[miss_y][miss_x] = temp_arr[miss_y][miss_x+1]
        temp_arr[miss_y][miss_x+1] = temp
        return temp_arr

        
    def move_left(self, miss_y, miss_x):

        temp_arr=copy.deepcopy(self.data)
        temp = temp_arr[miss_y][miss_x]
        temp_arr[miss_y][miss_x] = temp_arr[miss_y][miss_x-1]
        temp_arr[miss_y][miss_x-1] = temp
        return temp_arr
            
    def move_up(self, miss_y, miss_x):

        temp_arr=copy.deepcopy(self.data)
        temp = temp_arr[miss_y][miss_x]
        temp_arr[miss_y][miss_x] = temp_arr[miss_y-1][miss_x]
        temp_arr[miss_y-1][miss_x] = temp
        return temp_arr
            
    def move_down(self, miss_y, miss_x):

        temp_arr=copy.deepcopy(self.data)
        temp = temp_arr[miss_y][miss_x]
        temp_arr[miss_y][miss_x] = temp_arr[miss_y+1][miss_x]
        temp_arr[miss_y+1][miss_x] = temp
        return temp_arr
            
    def generate_states(self, finalout, visited, goalstate, nodesetout):
        final = finalout.copy()
        visitfinal = visited.copy()

        if (self.data == goal_state):
            return len(visited)
        
        temp_0 = self.find_miss()
        miss_y = int(temp_0[0])
        miss_x = int(temp_0[1])

        # Check for right movement
        if (miss_x !=2): 
            temp_right = Node(self.move_right(miss_y, miss_x), self)

            if Node.not_in(temp_right, visited):
                visited.insert(0, temp_right)
                final.insert(0,temp_right)

            if (temp_right.data == goal_state):
                return len(visited), temp_right

        # Check for left movement
        if (miss_x!=0):
            temp_left = Node(self.move_left(miss_y, miss_x), self)

            if Node.not_in(temp_left, visited):
                visited.insert(0,temp_left)
                final.insert(0,temp_left)

            if (temp_left.data == goal_state):
                return len(visited), temp_left

        # Check for up movement
        if (miss_y!=0):
            temp_up = Node(self.move_up(miss_y, miss_x), self)

            if Node.not_in(temp_up, visited):
                visited.insert(0,temp_up)
                final.insert(0,temp_up)

            if (temp_up.data == goal_state):
                return len(visited), temp_up

        # Check for down movement
        if (miss_y!=2):
            temp_down = Node(self.move_down(miss_y, miss_x), self)

            if Node.not_in(temp_down, visited):
                visited.insert(0,temp_down)
                final.insert(0,temp_down)

            if (temp_down.data == goal_state):
                return len(visited), temp_down

        if (final):    
            return Node.generate_states(final.pop(0), final, visited, goalstate, nodesetout)
        else: return 0

init = Node(initial_state, [0])
init.parent = [0]

finalout.append(init)
visitedout.append(init)

result, node = init.generate_states(finalout, visitedout, goal_state, visited_set)
ans_list = []
if (result):
    print("Solution found in", result,"iterations")
    print("Solution- ")
    while (node != [0]):
        ans_list.append(node.data)
        node = node.parent
    ans_list.reverse()
    print_rows(ans_list)

else: print("No solution found")
