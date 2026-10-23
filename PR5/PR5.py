# Вариант 10. Метод простой итерации (Якоби)
A = [[55, 18, 35],
     [56, -83, 17],
     [33, -24, -63]]
B = [43, 52, 95]
eps = 0.01
n = 3

x = [0.0] * n
k = 0
while True:
    k += 1
    new = [(B[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)) / A[i][i]
           for i in range(n)]
    delta = max(abs(new[i] - x[i]) for i in range(n))
    x = new
    if delta < eps:
        break

print(f"Итераций: {k}")
for i in range(n):
    print(f"x{i+1} = {x[i]:.4f}")
