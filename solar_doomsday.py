def solution(area):
    result = []
    # WHILE AREA IS GREATER THAN 0
    while area > 0:
        # DO A SQUARE ROOT OF AREA, BUT RETURN A STRICT WHOLE INTEGER WITH NO REMAINDER
        x = int(area ** 0.5)
        # SQUARE THE INTEGER
        y = x ** 2
        # SUBTRACT THE INTEGER FROM ORIGINAL AREA, AND SET THE RESULT AS NEW AREA
        area -= y
        # APPEND THE VALUE OF SQUARED INTEGER TO NEW LIST
        result.append(y)
    # RETURN RESULT
    return result


solution(area)
