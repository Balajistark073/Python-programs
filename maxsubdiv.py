def largest_divisible_by_90(n):
    if n.count(0) == 0:
        return -1  
    n.sort(reverse=True)  
    total = sum(n)
    if total % 3 != 0:
        return 0
    if n[0] == 0:
        return 0
    result = int(''.join(map(str, n)))
    return result
total_num = int(input())
input_list = list(map(int, input().split()))
result = largest_divisible_by_90(input_list)
print(result)