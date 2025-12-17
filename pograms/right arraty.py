n=len(list)
k%n 3%5
n[:k]=reversed(n[:k])
n[k:]=reversed(n[k:])

 right rotate

n = len(nums)
        k %= n
        if n < 2 or k == 0:
            return
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]