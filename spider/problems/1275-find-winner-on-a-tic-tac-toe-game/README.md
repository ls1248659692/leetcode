# [Find Winner on a Tic Tac Toe Game][title]

## Description

_A_ 和  _B_  在一个  _3_  x  _3_  的网格上玩井字棋。

井字棋游戏的规则如下：

  * 玩家轮流将棋子放在空方格 (" ") 上。
  * 第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
  * "X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
  * 只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
  * 如果所有方块都放满棋子（不为空），游戏也会结束。
  * 游戏结束后，棋子无法再进行任何移动。

给你一个数组 `moves`，其中每个元素是大小为 `2` 的另一个数组（元素分别对应网格的行和列），它按照 _A_ 和 _B_ 的行动顺序（先 _A_ 后
_B_ ）记录了两人各自的棋子位置。

如果游戏存在获胜者（ _A_ 或 _B_ ），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回
"Pending"。

你可以假设 `moves` 都 **有效** （遵循井字棋规则），网格最初是空的， _A_ 将先行动。



**示例 1：**
            **输入：** moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]    **输出：** "A"    **解释：** "A" 获胜，他总是先走。    "X  "    "X  "    "X  "    "X  "    " **X**  "    "   " -> "   " -> " X " -> " X " -> " **X** "    "   "    "O  "    "O  "    "OO "    "OO **X** "    

**示例 2：**
            **输入：** moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]    **输出：** "B"    **解释：** "B" 获胜。    "X  "    "X  "    "XX "    "XXO"    "XXO"    "XX **O** "    "   " -> " O " -> " O " -> " O " -> "XO " -> "X **O** "     "   "    "   "    "   "    "   "    "   "    " **O**  "    

**示例 3：**
            **输入：** moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]    **输出：** "Draw"    **输出：** 由于没有办法再行动，游戏以平局结束。    "XXO"    "OOX"    "XOX"    

**示例 4：**
            **输入：** moves = [[0,0],[1,1]]    **输出：** "Pending"    **解释：** 游戏还没有结束。    "X  "    " O "    "   "    



**提示：**

  * `1 <= moves.length <= 9`
  * `moves[i].length == 2`
  * `0 <= moves[i][j] <= 2`
  * `moves` 里没有重复的元素。
  * `moves` 遵循井字棋的规则。


**Tags:** Array, Hash Table, Matrix, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def tictactoe(self, m: List[List[int]]) -> str:
        def v1(m):
            seta = set(['%s%s'%(e[0],e[1]) for i,e in enumerate(m) if i%2==0])
            setb = set(['%s%s'%(e[0],e[1]) for i,e in enumerate(m) if i%2==1])
            for s in '00 11 22,02 11 20,00 01 02,10 11 12,20 21 22,00 10 20,01 11 21,02 12 22'.split(','):
                if set(s.split()).issubset(seta): return "A"
                if set(s.split()).issubset(setb): return "B"
            return "Draw" if len(m)==9 else 'Pending'

        def v2(m):
            onel=lambda s,rc:max([sum(e[rc]==str(i) for e in s) for i in range(3)])==3  
            crs=lambda s:set(['00','11','22']).issubset(s) or  set(['02','11','20']).issubset(s) 
            seta = set(['%s%s'%(e[0],e[1]) for i,e in enumerate(m) if i%2==0])
            setb = set(['%s%s'%(e[0],e[1]) for i,e in enumerate(m) if i%2==1])    
            if  onel(seta,0) or onel(seta,1) or crs(seta):return "A"    
            if  onel(setb,0) or onel(setb,1) or crs(setb):return "B"    
            return "Draw" if len(m)==9 else 'Pending'

        def v3(m):
            onel=lambda s,rc:max([sum(e[rc]==i for e in s) for i in range(3)])==3
            crs=lambda s:set([(i,i)for i in range(3)]).issubset(s) or  set([(i,2-i) for i in range(3)]).issubset(s) 
            seta = set([tuple(e) for i,e in enumerate(m) if i%2==0])
            setb = set([tuple(e) for i,e in enumerate(m) if i%2==1])
            if  onel(seta,0) or onel(seta,1) or crs(seta):return "A"    
            if  onel(setb,0) or onel(setb,1) or crs(setb):return "B"    
            return "Draw" if len(m)==9 else 'Pending'            
        return v3(m)
```

[title]: https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game
