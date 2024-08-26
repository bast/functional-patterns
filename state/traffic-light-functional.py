def red_light():
    print("Red Light - STOP!")
    return green_light


def green_light():
    print("Green Light - GO!")
    return yellow_light


def yellow_light():
    print("Yellow Light - SLOW DOWN!")
    return red_light


def traffic_light(initial_state, cycles):
    state = initial_state
    for _ in range(cycles):
        state = state()


if __name__ == "__main__":
    traffic_light(red_light, 6)
