# [Find All Possible Recipes from Given Supplies][title]

## Description

你有 `n` 道不同菜的信息。给你一个字符串数组 `recipes` 和一个二维字符串数组 `ingredients` 。第 `i` 道菜的名字为
`recipes[i]` ，如果你有它  **所有**  的原材料 `ingredients[i]` ，那么你可以  **做出**
这道菜。一道菜的原材料可能是  **另一道**  菜，也就是说 `ingredients[i]` 可能包含 `recipes` 中另一个字符串。

同时给你一个字符串数组 `supplies` ，它包含你初始时拥有的所有原材料，每一种原材料你都有无限多。

请你返回你可以做出的所有菜。你可以以 **任意顺序**  返回它们。

注意两道菜在它们的原材料中可能互相包含。



**示例 1：**
            **输入：** recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]    **输出：** ["bread"]    **解释：**    我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。    

**示例 2：**
            **输入：** recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]    **输出：** ["bread","sandwich"]    **解释：**    我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。    我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。    

**示例 3：**
            **输入：** recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]    **输出：** ["bread","sandwich","burger"]    **解释：**    我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。    我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。    我们可以做出 "burger" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 和 "sandwich" 。    

**示例 4：**
            **输入：** recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"]    **输出：** []    **解释：**    我们没法做出任何菜，因为我们只有原材料 "yeast" 。    



**提示：**

  * `n == recipes.length == ingredients.length`
  * `1 <= n <= 100`
  * `1 <= ingredients[i].length, supplies.length <= 100`
  * `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
  * `recipes[i], ingredients[i][j]` 和 `supplies[k]` 只包含小写英文字母。
  * 所有 `recipes` 和 `supplies` 中的值互不相同。
  * `ingredients[i]` 中的字符串互不相同。


**Tags:** Graph, Topological Sort, Array, Hash Table, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def findAllRecipes(self, rec: List[str], ig: List[List[str]], sup: List[str]) -> List[str]:
        ig,sup=[(rec[i],set(e)) for i,e in enumerate(ig)],set(sup)
        addr=[rec for rec,ing in ig if ing.issubset(sup)]
        tset,aset=set(addr),set(addr)
        while aset:
            _aset,aset=set(aset),set()
            for r in _aset:sup.add(r)
            aset= set([rec for rec,ing in ig if ing.issubset(sup) and rec not in tset])
            for p in aset:tset.add(p)
        return list(tset)
            
```

[title]: https://leetcode-cn.com/problems/find-all-possible-recipes-from-given-supplies
