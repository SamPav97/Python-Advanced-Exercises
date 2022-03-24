from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    while nums:
        kwargs["a"] += nums.popleft()
        if not nums:
            break
        kwargs["s"] -= nums.popleft()
        if not nums:
            break
        try:
            kwargs["d"] /= nums.popleft()
            if not nums:
                break
        except:
            pass
        kwargs["m"] *= nums.popleft()
        if not nums:
            break
    return kwargs




#print(math_operations(2, a=1))
print(math_operations(6, a=0, s=0, d=0, m=0))