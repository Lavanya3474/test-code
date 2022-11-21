def ternary(n):
    if (n == 0):
        return;
    r = n % 3;
    n //= 3;
    if (r < 0):
        n += 1;
    ternary(n);
    if (r < 0):
        print(r + (3 * -1), end = "");
    else:
        print(r, end = "");
def convert(Dec):
    print(Dec);
    if (Dec != 0):
        convert(Dec);
    else:
        print("0", end = "");
Dec = int(input(""))
ternary(Dec);
