# https://programmers.co.kr/learn/courses/30/lessons/42883

import numpy as np
import sys
sys.setrecursionlimit(10**6)

def sol1(number, k):
    if k==0:
        return number
    elif k == len(number):
        return None
    else:
        idx = np.argmax(number[:k+1])
        returned = sol1(number[idx+1:], k-idx)
        return np.concatenate((number[idx], returned), axis=None) if returned is not None else number[idx]

def solution1(number, k):
    number = np.asarray([*number]).astype(np.int)
    return ''.join(list(sol1(number, k).astype(np.str)))