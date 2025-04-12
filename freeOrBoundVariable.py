def extract_variables(expression):
    bound_vars = set()
    free_vars = set()
    scopes = []
    i = 0
    n = len(expression)

    while i < n:
        char = expression[i]

        if char in ('∀', '∃'):
            i += 1
            if i < n:
                var = expression[i]
                if scopes:
                    scopes[-1].add(var)
                else:
                    scopes.append(set([var]))
                i += 1
                if i < n and expression[i] == '(':
                    scopes.append(set([var]))
                    i += 1

        elif char == '(':
            scopes.append(set())
            i += 1

        elif char == ')':
            if scopes:
                scopes.pop()
            i += 1

        elif char.isupper():
            i += 1
            if i < n and expression[i] == '(':
                i += 1
                while i < n and expression[i] != ')':
                    if expression[i].islower():
                        var = expression[i]
                        found = any(var in scope for scope in reversed(scopes))
                        if found:
                            bound_vars.add(var)
                        else:
                            free_vars.add(var)
                    i += 1
                if i < n and expression[i] == ')':
                    i += 1

        else:
            i += 1

    free_vars -= bound_vars

    print('متغیرهای آزاد:', ''.join(sorted(free_vars)) if free_vars else 0)
    print('متغیرهای بسته:', ''.join(sorted(bound_vars)) if bound_vars else 0)


# فقط یکبار گرفتن ورودی
expression = input("لطفاً یک عبارت منطقی وارد کنید: ")
extract_variables(expression)
