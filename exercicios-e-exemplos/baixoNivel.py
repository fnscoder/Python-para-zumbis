import dis
print('Assembly de uma soma:')
dis.dis('c = a + b')

def f(n):
    k = 1
    f = 1
    while k <= n:
        f *= k
        k += 1
    return f

print('\nAssembly da função fatorial:')
dis.dis(f)
