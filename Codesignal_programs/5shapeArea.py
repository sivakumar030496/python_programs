def shapeArea(n):
    area = 1
    while n > 1:
        area += (n-1)*4
        n -= 1
    return area
