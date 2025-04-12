def extract_variables(expression):
    bound_vars = set()
    free_vars = set()
    scopes = []
    i = 0
    n = len(expression)

    while i < n:
        if expression[i] in ('∀', '∃'):
            i += 1
            var = expression[i]
            if scopes:
                scopes[-1].add(var)
            else:
                scopes.append(set([var]))
            i += 1
            if i < n and expression[i] == '(':
                scopes.append(set([var]))
                i += 1
        elif expression[i] == '(':
            scopes.append(set())
            i += 1
        elif expression[i] == ')':
            if scopes:
                scopes.pop()
            i += 1
        elif expression[i].isupper():
            i += 1
            if i < n and expression[i] == '(':
                i += 1
                while i < n and expression[i] != ')':
                    if expression[i].islower():
                        var = expression[i]
                        found = False
                        for scope in reversed(scopes):
                            if var in scope:
                                bound_vars.add(var)
                                found = True
                                break
                        if not found:
                            free_vars.add(var)
                    i += 1
                if i < n and expression[i] == ')':
                    i += 1
        else:
            i += 1

    free_vars = free_vars - bound_vars

    print(''.join(sorted(free_vars)) if free_vars else 0)
    print(''.join(sorted(bound_vars)) if bound_vars else 0)

examples = [
    "∀x(P(x)→∃yQ(y,x))",
    "P(x)∧∃y(Q(y)∨R(x,y))",
    "∀x(∃y(P(x,y)∧Q(z)))",
    "P(x,y)∨Q(z)",
    "∀x(P(x)∧Q(y))",
]

for idx, expr in enumerate(examples, 1):
    print(f"Example {idx}: {expr}")
    extract_variables(expr)
    print("---")
