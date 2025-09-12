
import json
with open("../src/rainbow.json", "r") as rainbow:
    payload = json.load(rainbow)
    rainbowColor = payload[0]["color"]


def isRainbowColor(color: str) -> bool:
    """_summary_

    Args:
        color (_str_): _string color name to be tested_

    Returns:
        _bool_: _expected boolean output_
    """
    #print(type(rainbowColor))
    # for targetColor in rainbowColor:
    #     if targetColor == color.lower():
    #         #print(targetColor)
    #         return True
    # return False
    #print(rainbowColor.read())
    return any(targetColor == color.lower() for targetColor in rainbowColor)