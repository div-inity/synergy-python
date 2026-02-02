str = input()
vowels = 'aeiou'
nums = [0,0,0,0,0]


for i in str :
    index = vowels.find(i)
    if i in vowels :
        nums[index] += 1

for i in vowels :
    index = vowels.find(i)
    if nums[index] != 0 :
        print(i, nums[index])
    else :
        print(i, "false")
