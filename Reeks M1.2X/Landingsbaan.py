def is_valid_angle(angle):
    return angle <= 360 and angle >= 0


def is_valid_runway(runway):
    val1, val2 = runway.split("/")
    val1 = int(val1)
    val2 = int(val2)
    return abs(val1 - val2) == 18


def get_runway(angle):
    runway = int(round(angle / 10))
    if runway > 18:
        runway_first = runway - 18
        runway_second = runway
    else:
        runway_first = runway
        runway_second = runway + 18

    if runway == 0:
        runway_first = 18
        runway_second = 36

    return f"{runway_first:02d}/{runway_second:02d}"


angle = float(input("Angle:"))
if is_valid_angle(angle):
    runway = get_runway(angle)
    if is_valid_runway(runway):
        print(runway)
