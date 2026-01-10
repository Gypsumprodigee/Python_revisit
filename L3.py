#list
users  = ['Dave','John','Sara']

data = ['Dave',43,True]

emptylist = []

print("Dave"in users)#True or false

print(users[0])
print(users[-1])
print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])
 
print(len(data))
 
users.append('Jake')
print(users)

users += ['Jason']# if no brackets it consider each letter individually
print(users)

users.extend(['Robert','Kim'])
print(users)

# users.extend(data)
# print(users)

users.insert(0,'Bob')
print(users)

users[2:2] = ['Eddie','Alex']# does not replace
print(users)

users[1:3] = ['Robert','JPJ']#refers to a slice(replace)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

#del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums,reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy.sort())
print(nums)

print(nums)
