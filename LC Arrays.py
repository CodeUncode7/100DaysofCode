#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 08:16:57 2023

@author: ainish
"""
class Solution:
    
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for element in nums:
            if len(str(element))%2 == 0:
                count+=1
        return count
    
    def sortedSquares_depracated(self, nums: list[int]) -> list[int]:
        result = []
        for element in nums:
            result.append(element*element)
        result.sort()
        return result

    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        i = 0
        while (i<N):
            if arr[i]!=0:
                i+=1
            else:
                for j in range(N-1, i, -1):
                    arr[j]=arr[j-1]
                i = i+2
        return
    
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for j in range(m, len(nums1)):
            nums1.pop(-1)
        for j in range(n,len(nums2)):
            nums2.pop(-1)
        while (True):
    
            if len(nums2) == 0:
                return
    
            if len(nums1) == 0 or len(nums1) == i:
                for element in nums2:
                    nums1.insert(i, element)
                    i+=1
                return
    
    
            if (nums1[i] > nums2[0]):
                nums1.insert(i,nums2.pop(0))
            i+=1
        return

    def removeElement(self, nums: list[int], val: int) -> int:
        N = len(nums)
        if N == 0:
            return
        i = 0
        while (i<N):
            if nums[i] == val:
                nums.pop(i)
                N = N-1
            else:
                i = i+1

        return

    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        current = nums[0]
        while (i < len(nums)):
            if nums[i] == current:
                nums.pop(i)
            else:
                current = nums[i]
                i+=1
        return
    
    def checkIfExist(self, arr: list[int]) -> bool:
        N = len(arr)
        for i in range(N-1):
            for j in range(N):
                if arr[i] == arr[j]/2 or arr[i]== arr[j]*2 :
                    if i!=j:
                        return True
        return False

    def validMountainArray(self, arr: list[int]) -> bool:
        N = len(arr)
        if N<3:
            return False
        if arr[0]>arr[1]:
            return False      
        for i in range(N-1):
            if arr[i]>=arr[i+1]:
                break
        if arr[i]==arr[i+1]:
            return False

        for j in range(i, N-1):
            if arr[j]<=arr[j+1]:
                return False
        return True

    def replaceElements(self, arr: list[int]) -> list[int]:
        N = len(arr)
        if N==1:
            arr[0]= -1
            return arr
        
        isgreatestknown = False
        for i in range(N-1):
            if isgreatestknown == False:
                greatest = -1            
                for j in range(i+1,N):
                    if arr[j] > greatest:
                        greatest = arr[j]
                        index = j
                    isgreatestknown = True
            arr[i] = greatest
            if i==index-1:
                isgreatestknown = False
        arr[-1] = -1
        return arr
    
    def moveZeroes(self, arr: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(arr)
        i = 0

        while(i<N):
            if arr[i] == 0:
                arr.pop(i)
                arr.append(0)
                N = N-1
                continue
            i+=1

        return

    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        j = len(nums) -1
        i = 0
        while i <j:
            if (nums[i]%2 > nums[j]%2):
                nums[i],nums[j] = nums[j],nums[i]
            if nums[i]%2 == 0:
                i+=1
            if nums[j]%2 !=0:
                j = j-1
        return nums

    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count+=1
        return count
    
    def thirdMax(self, nums: list[int]) -> int:
        largest = []
    
        for element in nums:
            if element in largest:
                continue

            if len(largest) <3:
                largest.append(element)
                largest.sort()
                continue       

            if element < largest[0]:
                continue

            largest.pop(0)
            largest.append(element)
            largest.sort()

        if len(largest)<3:
            return largest[-1]
        return largest[0]

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []
        
        for i in range(len(nums)):
            #make number at index nums[i] negetive to use as flag
            index = abs(nums[i])-1
            if nums[index] > 0: nums[index]=nums[index]*-1
        
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        
        
        return result
    
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        result = [] 
        left, right = 0,len(nums)-1
        
        while (right > left):
            if (abs(nums[right]) < abs(nums[left])):
                result.insert(0, nums[left]*nums[left])
                left+=1
                continue
            result.insert(0,nums[right]*nums[right])
            right = right -1
        result.insert(0, nums[right]*nums[right])
        return result
        
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left, right, zeros = 0,0,0
        longest = 1
        while right < len(nums):
            if nums[right] == 0:
                zeros+=1
            
            while zeros == 2:
                if nums[left] == 0:
                    zeros -=1
                left+=1
            
            longest = max(longest, right - left +1 )
            right+=1
        return longest
            

            
            