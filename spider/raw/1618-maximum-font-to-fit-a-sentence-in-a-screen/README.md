# [Maximum Font to Fit a Sentence in a Screen][title]

## Description

给定一个字符串 `text`。并能够在 宽为 `w` 高为 `h` 的屏幕上显示该文本。

字体数组中包含按 **升序排列** 的可用字号，您可以从该数组中选择任何字体大小。

您可以使用`FontInfo`接口来获取任何 **可用字体大小** 的任何字符的宽度和高度。

`FontInfo`接口定义如下：
            interface FontInfo {      // 返回 fontSize 大小的字符 ch 在屏幕上的宽度。      // 每调用该函数复杂度为 O(1)      public int getWidth(int fontSize, char ch);          // 返回 fontSize 大小的任意字符在屏幕上的高度。      // 每调用该函数复杂度为 O(1)      public int getHeight(int fontSize);    }

一串字符的文本宽度应该是 **每一个字符** 在对应字号`(fontSize)`下返回的宽度`getHeight(fontSize)`的 **总和** 。

**请注意：文本最多只能排放一排**

如果使用相同的参数调用 `getHeight` 或 `getWidth` ，则可以保证 `FontInfo` 将返回相同的值。

同时，对于任何字体大小的 `fontSize` 和任何字符 `ch` ：

  * `getHeight(fontSize) <= getHeight(fontSize+1)`
  * `getWidth(fontSize, ch) <= getWidth(fontSize+1, ch)`

返回可用于在屏幕上显示文本的最大字体大小。 **如果文本不能以任何字体大小显示，则返回-1** 。

**示例 1:**
            **输入:** text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]    **输出:** 6    

**Example 2:**
            **输入:** text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]    **输出:** 4    

**Example 3:**
            **输入:** text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]    **输出:** -1    

**注意:**

  * `1 <= text.length <= 50000`
  * `text` 只包含小写字母
  * `1 <= w <= 107`
  * `1 <= h <= 104`
  * `1 <= fonts.length <= 105`
  * `1 <= fonts[i] <= 105`
  * `fonts `已经按升序排序，且不包含重复项。


**Tags:** Array, String, Binary Search, Interactive

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-font-to-fit-a-sentence-in-a-screen
