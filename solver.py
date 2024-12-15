from data import HEADING
from data_structure import Node


class SearchPuzzle:

    def generateNode(self, current: Node) -> list:
        '''
        Hàm sinh tất cả trạng thái có thể có và trả về dạng list.
        '''
        ans = []    
        for i in range(5):
            for j in range(5):             
                for k in HEADING:                   
                    if current.state.head[i][j]["heading"] == k:
                        continue   
                    newNode = Node(current.state.head,[i,j],current)

                    newNode.state.head[i][j]["heading"] = k
                    newNode.state.rotate(i, j)
                    newNode.step = current.step + 1
                    ans.append(newNode)
        return ans
    
    def getPath(self, end_node: Node) -> list:
        '''
        Trả về list các state từ state đầu tiên
        '''
        ans = []
        temp = end_node
        while temp:
            ans.insert(0,temp.state)
            temp = temp.previous
        return ans

    def hx(self, current: Node) -> int:
        ans = -5* current.state.countPumped
        if current.previous != None:
            if current.state.countPumped == current.previous.state.countPumped:
                for i in range(5):
                    for j in range(5):
                        if current.state.head[i][j]["pumped"] != current.previous.state.head[i][j]["pumped"]:
                            ans -= 2
                            break
                        elif current.state.head[i][j]["pumped"] and current.previous.state.head[i][j]["pumped"]:
                            if current.state.head[i][j]["heading"] != current.previous.state.head[i][j]["heading"]:
                                ans -= 2
                                break
                else:
                    ans += 2
        
        if current.state.countPumped:
            for i in [0,4]:
                for j in range(5):
                    list1 = current.state.getAngle(current.state.head[i][j])
                    if i == 0:
                        if 90 in list1:
                            ans += 1
                            if current.state.head[i][j]["pumped"]:
                                ans += 5
                        else:
                            ans -= 2
                    if i == 4:
                        if 270 in list1:
                            ans += 1
                            if current.state.head[i][j]["pumped"]:
                                ans += 5
                        else:
                            ans -= 2
            
            for j in [0,4]:
                for i in range(5):
                    list1 = current.state.getAngle(current.state.head[i][j])
                    if j == 0 and 180 in list1:
                        ans += 1
                        if current.state.head[i][j]["pumped"]:
                            ans += 5
                    else: ans -= 2
                    if j == 4 and 0 in list1:
                        ans += 1   
                        if current.state.head[i][j]["pumped"]:
                            ans += 5
                    else:
                        ans -= 2     

        # Xem có vòng lặp không: state, oy,ox
        if current.state.checkLoop(current.rotate[0], current.rotate[1]):
            ans += 2000
        return ans 

    def gx(self, current: Node):
        if current == None:
            return 0
        return current.step*2

    def fx(self, current: Node) -> int:
        return self.gx(current) + self.hx(current)

    def solve_Astar(self, init_state: list):
        """
        Best First Search for the path from init_state to goal_state and save in self.path
        """
        head = Node(init_state, [2,2], None)
        head.heuristics = self.fx(head)
        head.step = 0
        
        # openList = [heristics, step, state]
        openList = [[self.fx(head),head]]

        #dict for statistic
        dataForPlot = {0:1}
        closeList = []
        while len(openList) != 0:
            current_state = openList.pop(0)

            #add new step to dataForPlot if its doesn't have step key, else increase step value.
            if current_state[1].step not in dataForPlot:
                dataForPlot.update({current_state[1].step:1})
            else:
                dataForPlot[current_state[1].step] += 1

            if current_state[1] not in closeList:
                closeList.append(current_state[1])
                if current_state[1].state.countPumped  == 25:
                    print("Solution found")
                    break
                newStateList = self.generateNode(current_state[1])
                for newNode in newStateList:
                    if newNode not in closeList and newNode not in(obj for obj in openList):
                        openList.append([self.fx(newNode), newNode]) 
                # Sắp xếp openList theo thứ tự tg nào có heuristics nhỏ hơn ưu tiên trước.
                openList.sort(key=lambda x: int(x[0]))
        print("Number of state: ", len(openList) + len(closeList))

        return dataForPlot, self.getPath( closeList.pop(len(closeList) - 1))

    def solve_dfs(self, init_state: list) -> list:
        """
        DFS for the path from init_state to goal_state and save in self.path
        """
        stack = []
        visited = []
        first_node = Node(init_state, [0,0], None)
        stack.append(first_node)
        while len(stack) > 0:
            current_node = stack.pop(0)
            visited.append(current_node)

            if current_node.state.countPumped == 25:
                return self.getPath(current_node)
            
            successors = self.generateNode(current_node)
            for item in successors:
                if item not in visited and item not in stack:
                    stack.append(item)     

        return self.getPath(visited[len(visited) - 1]) 