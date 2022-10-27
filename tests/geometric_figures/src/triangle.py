def triangle(a,b,c):
    if a + b > c and a+c > b and b+c > a:
        if a == b and a == c:
            return 'equilateral_triangle'
        elif a == b or a== c or b==c:
            return 'isoceles_triangle'
        else:
            return 'scalene_triangle'
    else:
        return 'it_is_not_triangle'