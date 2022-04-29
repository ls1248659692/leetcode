class Solution:
    def orchestraLayout(self, num, xPos, yPos):
        inner = max(abs(2 * xPos - num + 1), abs(2 * yPos - num + 1)) - 1
        nn, mi, ma = num ** 2 - (inner + 2) ** 2, (num - inner) // 2 - 1, (num + inner) // 2
        nn += 1 + yPos - mi if xPos == mi else 2 + inner + xPos - mi if yPos == ma else 3 + 2 * inner + ma - yPos if xPos == ma else 4 + inner * 3 + ma - xPos
        return (nn - 1) % 9 + 1