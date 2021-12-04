def solution(drum):
    answer = 0
    for i in range(len(drum)):
        starCnt = 0
        j,k = 0,i
        while starCnt < 2 and j < len(drum):
            instr =drum[j][k]
            if instr == '#':
                j+=1
            elif instr == '>':
                k+=1
            elif instr == '<':
                k-=1
            elif instr == '*':
                if starCnt < 1: 
                    j+=1
                starCnt +=1
        if j == len(drum):
            answer+=1
    return answer

print(solution(["######",">#*###","####*#","#<#>>#",">#*#*<","######"]))# , 4