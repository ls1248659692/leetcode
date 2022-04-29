# [Minimum Swaps to Make Strings Equal][title]

## Description

有两个长度相同的字符串 `s1` 和 `s2`，且它们其中  **只含有**  字符 `"x"` 和
`"y"`，你需要通过「交换字符」的方式使这两个字符串相同。

每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。

交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 `s1[i]` 和 `s2[j]`，但不能交换 `s1[i]`
和 `s1[j]`。

最后，请你返回使 `s1` 和 `s2` 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 `-1` 。



**示例 1：**
            **输入：** s1 = "xx", s2 = "yy"    **输出：** 1    **解释：** 交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。

**示例 2：**
            **输入：** s1 = "xy", s2 = "yx"    **输出：** 2    **解释：** 交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。    交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。    注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。

**示例 3：**
            **输入：** s1 = "xx", s2 = "xy"    **输出：** -1    

**示例 4：**
            **输入：** s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"    **输出：** 4    



**提示：**

  * `1 <= s1.length, s2.length <= 1000`
  * `s1, s2` 只包含 `'x'` 或 `'y'`。


**Tags:** Greedy, Math, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if  len(s1)!=len(s2) or (s1+s2).count('x')%2==1: return -1 
        di =[i for i in range(len(s1)) if s1[i]!=s2[i]]
        d1,d2= ''.join([s1[i] for i in di]),''.join([s2[i] for i in di])
        sm = len(di)
        xd = abs(s1.count('x')-s2.count('x'))
        print(len(s1),d1,d2,sm,xd)
        if sm==0:return 0
        #if sm >= abs(s1.count('x')-s2.count('x')):
        # yy.xx 2 yx.xy 2  yyyy.xxxx 2 yyyx.yyxy 3 yxyx xyxy 2
        #(2,2)=1 (2,0)=2 (4,4)=2 (4,2)=3 (4,0)=2 (6,6)=3 (6,4)=4 (6,2)=3 (6,0)=4
        # len xdA xdB xdC 
        # 2: 2=1 0=2  
        # 4: 4=2 2=3 0=2
        # 6: 6=3 4=4 2=3 0=4
        # 8: 8=4 6=5 4=4 2=5 0=4
        #10:10=5 8=6 6=5 4=6 2=5 0=6
                                # 6
                                #8
                                #8
                                #10


        if len(s1)<=1000:
            return sm//2+(sm//2-xd//2)%2
```

[title]: https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal
