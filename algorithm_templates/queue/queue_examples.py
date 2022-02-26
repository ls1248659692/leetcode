from collections import deque


# [513] https://leetcode.com/problems/find-bottom-left-tree-value/
# Given a binary tree, find the leftmost value in the last row of the tree.
# widely used in BFS
def findBottomLeftValue(root):
    queue = deque([root])

    def bfs():
        while len(queue):
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val

    return bfs()


# [346] https://leetcode.com/problems/moving-average-from-data-stream/
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.cur_size = 0
        self.sum = 0

    def next(self, val: int) -> float:
        if self.cur_size < self.size:
            self.cur_size += 1
        else:
            self.sum -= self.queue.popleft()

        self.queue.append(val)
        self.sum += val

        return self.sum / self.cur_size


# [225] https://leetcode.com/problems/implement-stack-using-queues/
# Implement the following operations of a stack using queues.
class MyStack:
    def __init__(self):
        self.queues = [deque(), deque()]
        self.cur_index = 0

    def push(self, x: 'int') -> 'None':
        self.queues[self.cur_index].append(x)
        if len(self.queues[self.cur_index]) > 1:
            self.queues[1 - self.cur_index].append(self.queues[self.cur_index].popleft())

    def pop(self) -> 'int':
        res = self.queues[self.cur_index].popleft()
        while len(self.queues[1 - self.cur_index]) > 1:
            self.queues[self.cur_index].append(self.queues[1 - self.cur_index].popleft())
        self.cur_index = 1 - self.cur_index
        return res

    def top(self) -> 'int':
        return self.queues[self.cur_index][0]

    def empty(self) -> 'bool':
        return not self.queues[0] and not self.queues[1]


# [353] https://leetcode.com/problems/design-snake-game/
# Design a Snake game that is played on a device with screen size = width x height
#
# double-ended queue
class SnakeGame:
    def __init__(self, width: int, height: int, food: 'List[List[int]]'):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.food, self.food_idx = food, 0
        self.snake = deque([[0, 0]])
        self.size = (height, width)
        self.dirs = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        self.res = 0

    def move1(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        pos = [self.snake[0][0] + self.dirs[direction][0], self.snake[0][1] + self.dirs[direction][1]]
        if pos[0] < 0 or pos[0] >= self.size[0] or pos[1] < 0 or pos[1] >= self.size[1]:
            return -1
        if self.food_idx < len(self.food) and pos == self.food[self.food_idx]:
            self.snake.appendleft(pos)
            self.food_idx += 1
        else:
            # notice first remove tail then check collision
            self.snake.pop()
            if pos in self.snake:
                return -1
            else:
                self.snake.appendleft(pos)
        return len(self.snake) - 1

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        pos = [self.snake[-1][0] + self.dirs[direction][0], self.snake[-1][1] + self.dirs[direction][1]]
        if pos[0] < 0 or pos[0] >= self.size[0] or pos[1] < 0 or pos[1] >= self.size[1]:
            return -1
        if self.food_idx < len(self.food) and pos == self.food[self.food_idx]:
            self.snake.append(pos)
            self.food_idx += 1
            self.res += 1
        else:
            # notice first remove tail then check collision
            self.snake.popleft()
            if pos in self.snake:
                return -1
            else:
                self.snake.append(pos)
        return self.res


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
