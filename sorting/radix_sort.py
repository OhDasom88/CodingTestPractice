import math

def counting_sort(A, digit, radix):
    # "A" is a list to be sorted, radix is the base of the number system, digit is the digit
    # we want to sort by

    # create a list B which will be the sorted list
    B = [0] * len(A)
    C = [0] * int(radix)
    # counts the number of occurrences of each digit in A 
    for i in range(0, len(A)):
        digit_of_Ai = (A[i] // radix ** digit) % radix
        C[digit_of_Ai] = C[digit_of_Ai] + 1
        # now C[i] is the value of the number of elements in A equal to i

    # this for loop changes C to show the cumulative # of digits up to that index of C
    for j in range(1, radix):
        C[j] = C[j] + C[j - 1]# base 별 자리를 군별로 입력할수 있도록 수정 2진수 1,3,5 등[1]은 뒤로 2,4 등[0]은 앞으로
        # here C is modifed to have the number of elements <= i
    for m in range(len(A) - 1, -1, -1): # to count down (go through A backwards)
        digit_of_Ai = (A[m] // radix ** digit) % radix
        C[digit_of_Ai] = C[digit_of_Ai] - 1# base별 자리군의 값을 지움
        B[C[digit_of_Ai]] = A[m]

    return B

def radix_sort(A, radix):
    # radix is the base of the number system
    # k is the largest number in the list
    k = max(A)
    # output is the result list we will build
    output = A
    # compute the number of digits needed to represent k
    digits = int(math.floor(math.log(k, radix) + 1))
    for i in range(digits):
        output = counting_sort(output, i, radix)

    return output

A = [11, 10, 3, 14, 12, 2, 8, 15, 2]
radix_sort(A, 2)