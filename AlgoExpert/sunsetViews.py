def sunsetViews(buildings, direction):
    # Write your code here.
    stack = []
    current_building = 0
    startIndex = 0 if direction == "WEST" else len(buildings)-1
    step = 1 if direction == "WEST" else -1

    idx = startIndex
    while idx >= 0 and idx < len(buildings):
        buildings_height = buildings[idx]
        if current_building < buildings_height:
            stack.append(idx)

        current_building = max(current_building, buildings_height)
        idx += step

    if direction == "EAST":
        return stack[::-1]
    return stack
