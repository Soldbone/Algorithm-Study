compressed_ipv6 = input()

if "::" in compressed_ipv6:
    left, right = compressed_ipv6.split("::")

    # "ab:cd:" -> [ab, cd, '']
    # "" -> []이어야 되는데 [""] 이게 나오므로 따로 처리
    left_groups = [group for group in left.split(":")] if left else []
    right_groups = [group for group in right.split(":")] if right else []

    missing = 8 - (len(left_groups) + len(right_groups))
    groups = left_groups  + missing * ["0000"] + right_groups

else:
    groups = compressed_ipv6.split(":")

print(":".join([group.zfill(4) for group in groups]))