# [Simple Bank System][title]

## Description

你的任务是为一个很受欢迎的银行设计一款程序，以自动化执行所有传入的交易（转账，存款和取款）。银行共有 `n` 个账户，编号从 `1` 到 `n`
。每个账号的初始余额存储在一个下标从 **0** 开始的整数数组 `balance` 中，其中第 `(i + 1)` 个账户的初始余额是
`balance[i]` 。

请你执行所有 **有效的** 交易。如果满足下面全部条件，则交易 **有效** ：

  * 指定的账户数量在 `1` 和 `n` 之间，且
  * 取款或者转账需要的钱的总数 **小于或者等于** 账户余额。

实现 `Bank` 类：

  * `Bank(long[] balance)` 使用下标从 **0** 开始的整数数组 `balance` 初始化该对象。
  * `boolean transfer(int account1, int account2, long money)` 从编号为 `account1` 的账户向编号为 `account2` 的账户转帐 `money` 美元。如果交易成功，返回 `true` ，否则，返回 `false` 。
  * `boolean deposit(int account, long money)` 向编号为 `account` 的账户存款 `money` 美元。如果交易成功，返回 `true` ；否则，返回 `false` 。
  * `boolean withdraw(int account, long money)` 从编号为 `account` 的账户取款 `money` 美元。如果交易成功，返回 `true` ；否则，返回 `false` 。



**示例：**
            **输入** ：    ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]    [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]    **输出：**    [null, true, true, true, false, false]        **解释：**    Bank bank = new Bank([10, 100, 20, 50, 30]);    bank.withdraw(3, 10);    // 返回 true ，账户 3 的余额是 $20 ，所以可以取款 $10 。                             // 账户 3 余额为 $20 - $10 = $10 。    bank.transfer(5, 1, 20); // 返回 true ，账户 5 的余额是 $30 ，所以可以转账 $20 。                             // 账户 5 的余额为 $30 - $20 = $10 ，账户 1 的余额为 $10 + $20 = $30 。    bank.deposit(5, 20);     // 返回 true ，可以向账户 5 存款 $20 。                             // 账户 5 的余额为 $10 + $20 = $30 。    bank.transfer(3, 4, 15); // 返回 false ，账户 3 的当前余额是 $10 。                             // 所以无法转账 $15 。    bank.withdraw(10, 50);   // 返回 false ，交易无效，因为账户 10 并不存在。    



**提示：**

  * `n == balance.length`
  * `1 <= n, account, account1, account2 <= 105`
  * `0 <= balance[i], money <= 1012`
  * `transfer`, `deposit`, `withdraw` 三个函数， **每个** 最多调用 `104` 次


**Tags:** Design, Array, Hash Table, Simulation

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/simple-bank-system
