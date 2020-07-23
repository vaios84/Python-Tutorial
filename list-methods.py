print("######### nums ##########")
nums = [8, 5, 7, 9, 1, 2, 4]
print(nums)

nums.append(20) #adds the new item at the end
print(nums)

nums.insert(2, 152) # go to index 2 and insert 152
print(nums)

nums.remove(8)
print(nums)

nums.pop() #remove the last item of the list
print(nums)


print(nums.index(7))

print(78 in nums)
print(9 in nums)

print("######### nums2 ##########")
nums2 = [8, 5, 8, 9, 1, 8, 4, 12, 74, 0]
print(nums2)

nums3 = nums2.copy()
print(nums3)

print("Appearances of the number 8:")
print(nums2.count(8))

nums2.remove(12)
print(nums2)
nums2.sort()
print(nums2)

nums2.reverse()

print(nums2)
print("nums3: ")
print(nums3)

nums2.clear()
print("nums2: ")
print(nums2)
