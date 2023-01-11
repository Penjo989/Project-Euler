
def decrypt(a, b, c, data):
    for i in range(len(data)):
        if i % 3 == 0:
            data[i] = data[i] ^ a
        elif i % 3 == 1:
            data[i] = data[i] ^ b
        else:
            data[i] = data[i] ^ c
        if (data[i] >= 97 and data[i] <= 122) or (data[i] >= 32 and data[i] <= 90):
            pass
        else:
            return ""


    d = [chr(i) for i in data]
    string = "".join(d)
    return string


def printData(data):
    d = [chr(i) for i in data]
    string = "".join(d)
    print(string)

def main():
    f = open('59 cipher.txt', 'r')
    g = open('words.txt', 'r')
    words = g.readlines()
    words = [word.strip() for word in words]
    line = f.readline()
    maximum = 0
    string = ""
    decryption = [0, 0 ,0]
    data = line.split(",")
    data = [int(i) for i in data]
    for a in range(ord('a'), ord('z') + 1):
        print(a)
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                string = decrypt(a, b, c, data)
                if string != "":
                    print(string)
    print(string)


if __name__ == "__main__":
    main()