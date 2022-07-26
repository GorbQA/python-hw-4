
def twoSum(nums, target):
    arr_nums=nums.copy()
    rez=target
    index=[]
    for i in range(len(arr_nums)):
        for j in range(i+1, len(arr_nums)):
            if (rez-arr_nums[i])!=arr_nums[j]:
                continue
            else:
                index.append(i)
                index.append(j)
    return(index)
try:
    nums_inp=list(map(int, input("Enter numbers separated by commas/ ").split(',')))
    sum_inp=int(input("Enter sum "))
    print('Array index of terms',twoSum(nums_inp,sum_inp))
except ValueError:print('Type only numbers')