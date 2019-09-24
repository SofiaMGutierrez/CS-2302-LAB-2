#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:30:06 2019
Course: CS 2302
Author: Sofia Gutierrez
Lab #2: Program created to find the kth smallest value in a list.
Instructor: Olac Fuentes
T.A.: Anindita Nath
"""
import time

L = []
n = int(input("Enter the desired length of your list: "))
for i in range(0, n):
    elements = int(input("Enter element number: "))
    L.append(elements)
print(L)
print("The kth smallest element in your list will print")
k = int(input("Insert k: "))

#bubble sort
start_time = time.time()
def select_bubble(L, k):
    for i in range (len(L)-1):
        for j in range (len(L)-1-i): #-i becuase last element(s) is/are already sorted
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j] #swaps first element with second element
    return L[k]


#quicksort using recursion
def partition(L, low, high):
    i = (low-1)
    pivot = L[high] #sets pivot to the last element in the list
    for j in range(low, high):
        #only if current element is less than the pivot
        #i will increment and and elements i and j will swap
        if L[j] <= pivot:
            i = i+1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[high] = L[high], L[i+1] #pivot is moved to position i+1
    return (i+1) #new pivot position is returned

start_time = time.time()
def select_quick(L, low, high):
    if low < high:
        p = partition(L, low, high)
        select_quick(L, low, p-1) #arranges left partition
        select_quick(L, p+1, high) #arrages right partition


#quicksort using a stack
def partition_stack(L, low, high):
    i = (low-1)
    pivot = L[high]
    for j in range(low, high):
        if L[j] <= pivot:
            i = i+1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[high] = L[high], L[i+1]
    return (i+1)

start_time = time.time()
def quick_stack(L, low, high):
    
    size = high - low + 1 #creates a stack
    stack = [0] * (size)
    top = -1
    top = top + 1 #push low
    stack[top] = low
    top = top + 1 #push high
    stack[top] = high
    
    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        
        pivot = partition_stack(L, low, high)
        
        if pivot - 1 > 1:
            top = top + 1
            stack[top] = 1
            top = top + 1
            stack[top] = pivot - 1
        
        if pivot + 1 < high:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high


#modified quicksort with one recursive call
def partition_modified(L, low, high):
    i = (low-1)
    pivot = L[high]
    for j in range(low, high):
        if L[j] <= pivot:
            i = i+1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[high] = L[high], L[i+1]
    return (i+1)

start_time = time.time()
def select_modified_quick(L, low, high, k):
    while low < high:
        pivot = partition_modified(L, low, high)
        if k < pivot:
            select_modified_quick(L, low, pivot-1, k)
            return L[k]
        elif k == pivot:
            return L[k]
        elif k > pivot:
            select_modified_quick(L, pivot+1, high, k)
            return L[k]

# modified quicksort without recursion or stacks
def partition_modified2(L, low, high):
    i = (low-1)
    pivot = L[high]
    for j in range(low, high):
        if L[j] <= pivot:
            i = i+1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[high] = L[high], L[i+1]
    return (i+1)

start_time = time.time()
def select_modified_quick2(L, low, high, k):
    while low < high:
        pivot = partition_modified2(L, low, high)
        while pivot != k:
            if k < pivot:
                pivot = partition_modified2(L, low, pivot-1)
            elif k > pivot:
                pivot = partition_modified2(L, pivot+1, high)
        return L[pivot]


print("Now select how you would like to find your kth element")
print("1: Bubble sort")
print("2: Quicksort using recursion")
print("3: Quicksort using a stack")
print("4: Modified quicksort with one recursive call")
print("5: Modified quicksort with only a while loop")
user_choice = int(input("Enter a menu number option: "))

if user_choice == 1:
    print("kth smallest value using bubble sort: ")
    print(select_bubble(L, k))
    bubble_time = time.time() - start_time
    print("Time it took to find the kth value: ")
    print(bubble_time)
elif user_choice == 2:
    print("kth smallest value using qicksort using recursion: ")
    select_quick(L, 0, len(L)-1)
    print(L[k])
    quick_time = time.time() - start_time
    print("Time it took to find the kth value: ")
    print(quick_time)
elif user_choice == 3:
    print("kth smallest value using qicksort using a stack: ")
    quick_stack(L, 0, len(L)-1)
    print(L[k])
    quick_stack_time = time.time() - start_time
    print("Time it took to find the kth value: ")
    print(quick_stack_time)
elif user_choice == 4:
    print("kth smallest value using modified qicksort with one recursive call: ")
    select_modified_quick(L, 0, len(L)-1, k)
    print(L[k])
    quick_modified_time = time.time() - start_time
    print("Time it took to find the kth value: ")
    print(quick_modified_time)
elif user_choice == 5:
    print("kth smallest value using modified qicksort with no recursive calls or stacks: ")
    print(select_modified_quick2(L, 0, len(L)-1, k))
    quick_modified_time2 = time.time() - start_time
    print("Time it took to find the kth value: ")
    print(quick_modified_time2)
else:
    print("Invalid input!")