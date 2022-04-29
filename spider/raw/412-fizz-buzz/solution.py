class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_get = []
        for i in range(1,n+1):
            if i % 15 == 0:
                list_get.append('FizzBuzz')
            elif i % 3 == 0:
                list_get.append('Fizz')
            elif i % 5 == 0:
                list_get.append('Buzz')
            else:
                list_get.append(str(i))
        return list_get