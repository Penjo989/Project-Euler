
def isSpecial(numerator, denominator):
    numeStr = str(numerator)
    denoStr = str(denominator)
    for i in range(1, 10):
        if str(i) in numeStr and str(i) in denoStr:
            try:
                if removeDigits(numeStr, str(i)) / removeDigits(denoStr, str(i)) == numerator / denominator:
                    return True
            except:
                pass
    return False

def removeDigits(strNum1, digit):
    if strNum1[0] == digit:
        return int(strNum1[1:])
    else:
        return int(strNum1[:1])



def main():
    d = 1
    n = 1
    for nume in range(10, 100):
        for deno in range(nume + 1, 100):
            if isSpecial(nume, deno):
                d *= deno
                n *= nume
    i = 2
    while n >= i:
        if n % i == 0 and d % i == 0:
            n /= i
            d /= i
        else:
            i += 1
    print(f"{n} / {d}")

main()