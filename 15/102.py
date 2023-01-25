
def cutsXAxix(p1, p2):
    p1 = [int(p1[0]), int(p1[1])]
    p2 = [int(p2[0]), int(p2[1])]
    if p1[0] == p2[0]:
        if p1[1] * p2[1] <= 0:
            if p1[0] == 0:
                return "mid"
            return "left" if p1[0] < 0 else "right"
        else:
            return False
    m = (p1[1] - p2[1]) / (p1[0] - p2[0])
    if m == 0:
        if p1[1] == 0:
            if p1[0] * p2[0] <= 0:
                return "mid"
            return "left" if p1[0] < 0 else "right"
        return False
    b = p1[1] - m * p1[0]
    x = -b / m
    if not (p2[0] <= x <= p1[0] or p1[0] <= x <= p2[0]):
        return False
    if x == 0: return "mid"
    return "left" if x < 0 else "right"



def main():
    f = open("102triangles.txt", "r")
    lines = f.readlines()

    triangles = []
    for line in lines:
        numbers = line.split(",")

        triangles.append([[numbers[0], numbers[1]], [numbers[2], numbers[3]], [numbers[4], numbers[5]]])

    sum = 0
    print(triangles[0])
    for triangle in triangles:
        axisPoints = [cutsXAxix(triangle[0], triangle[1]), cutsXAxix(triangle[1], triangle[2]),
                      cutsXAxix(triangle[0], triangle[2])]
        if "mid" in axisPoints or ("right" in axisPoints and "left" in axisPoints):
            print(f"({triangle[0]}), ({triangle[1]}), ({triangle[2]})")
            sum += 1
    print(sum)

main()