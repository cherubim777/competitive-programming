class Solution:
    def sortSentence(self, s: str) -> str:
        input = s.split(' ')
        output = ['' for _ in range(len(input))]
        
        for i in range(len(input)):
            output[int(input[i][-1])-1] = input[i][:-1]
            s = ' '.join(output)
        return s
