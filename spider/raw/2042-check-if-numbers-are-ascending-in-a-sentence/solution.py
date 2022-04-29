class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        str1 = ''
        for i in s:
            if i in '1234567890 ':
                str1 = str1 + i

        list1 = [int(i) for i in str1.split(' ') if i != '']
        for value in range(len(list1)-1):
            if list1[value] >= list1[value+1]:
                return False
                break
        return True