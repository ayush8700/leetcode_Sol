class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prevans = ""
        prevans += self.countAndSay(n-1)
        count = 1
        newans = ""
        for i in range(len(prevans) - 1):
            if prevans[i] == prevans[i+1]:
                count += 1
                continue
            newans += str(count) + prevans[i]
            count = 1
        newans += str(count) + prevans[len(prevans) -1]
        return newans