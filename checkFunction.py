def check_function():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    k = int(input())                    

    mapping = []
    for _ in range(k):
        a, b = map(int, input().split())
        mapping.append((a, b))

    a_to_b = dict()
    is_function = True
    for a, b in mapping:
        if a in a_to_b:
            if a_to_b[a] != b:
                is_function = False
                break
        else:
            a_to_b[a] = b

    if not is_function:
        print("Function: No")
        print("Injective: No")
        print("Surjective: No")
        print("Bijective: No")
        return

    b_seen = dict()
    is_injective = True
    for a, b in a_to_b.items():
        if b in b_seen:
            is_injective = False
            break
        else:
            b_seen[b] = a

    is_surjective = True
    for b in B:
        if b not in a_to_b.values():
            is_surjective = False
            break

    is_bijective = is_injective and is_surjective

    print(f"Function: {'Yes' if is_function else 'No'}")
    print(f"Injective: {'Yes' if is_injective else 'No'}")
    print(f"Surjective: {'Yes' if is_surjective else 'No'}")
    print(f"Bijective: {'Yes' if is_bijective else 'No'}")

check_function()
