"""
/**
 * @param {string} ??? - the color to check
 * @returns {boolean} whether or not the given color is a rainbow color
 */
"""
import json
with open("src/rainbow.json") as rainbow:
    payload = json.load(rainbow)
    rainbowColor = payload[0]["color"]


def isRainbowColor(color):
    #print(type(rainbowColor))
    for targetColor in rainbowColor:
        if targetColor == color.lower():
            #print(targetColor)
            return True
    return False