x, y, z = 3.3, 3.5, 3.7
a, b, c = -3.3, -3.5, -3.7

print(f"|{'val':>5}|{'int':>6}|{'//':>6}|{'format'}|")
print(f"|{x:>5}|{int(x):>6}|{x//1:>6.0f}|{x:6.0f}|")
print(f"|{y:>5}|{int(y):>6}|{y//1:>6.0f}|{y:6.0f}|")
print(f"|{z:>5}|{int(z):>6}|{z//1:>6.0f}|{z:6.0f}|")
print(f"|{a:>5}|{int(a):>6}|{a//1:>6.0f}|{a:6.0f}|")
print(f"|{b:>5}|{int(b):>6}|{b//1:>6.0f}|{b:6.0f}|")
print(f"|{c:>5}|{int(c):>6}|{c//1:>6.0f}|{c:6.0f}|")