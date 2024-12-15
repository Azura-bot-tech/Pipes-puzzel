"""
Note:
    In each level 5x5 Pipes:
        set index (x, y) start with bottom-left = (0, 0)
        increase x when through to top
        increase y when through to right
        each cell is a dict with two keys: type, heading.

    key ["type"]:
        value = 0 == images/type_0
        value = 1 == images/type_1
        value = 2 == images/type_2
        value = 3 == images/type_3
        value = 4 == images/type_4

    key ["heading"]:
        value = 0 == Eastern 
        value = 90 == Southern
        value = 180 == Western
        value = 270 == Northern 
        further, each image in images/ are approriate to Eastern
"""

HEADING = [0, 90, 180, 270]


TESTCASE = {
    "level1":[
        [
            {
                "type": 3,
                "heading":90,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type":3,
                "heading":0,
            },
            {
                "type": 1,
                "heading":180,
            },
            {
                "type": 1,
                "heading":0,
            },
        ],
        [
            {
                "type": 1,
                "heading":90,
            },
            {
                "type":2,
                "heading":90,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 3,
                "heading":90,
            },
            {
                "type": 2,
                "heading": 90,
            },
        ],
        [
            {
                "type": 1,
                "heading":270,
            },
            {
                "type": 1,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 4,
                "heading": 0,
            },
        ],
        [
            {
                "type": 3,
                "heading":90,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 2,
                "heading":0,
            },
        ],
        [
            {
                "type": 1,
                "heading": 180, 
            },
            {
                "type": 3,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 270,
            },
            {
                "type": 1,
                "heading": 0,
            },
        ],
    ],
        "level2":[
        [
            {
                "type": 1,
                "heading": 180,
            },
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type":3,
                "heading":90,
            },
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 90,
            },
        ],
        [
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 3,
                "heading": 270,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 270,
            },
        ],
        [
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 2,
                "heading": 90,
            },
            {
                "type": 2,
                "heading": 90,
            },
        ],
        [
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 1,
                "heading": 270,
            },
            {
                "type": 1,
                "heading": 270,
            },
        ],
        [
            {
                "type": 1,
                "heading": 0, 
            },
            {
                "type": 2,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 2,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 270,
            },
        ],
    ],
    "level3":[
        [
            {
                "type": 3,
                "heading": 180,
            },
            {
                "type": 1,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 270,
            },
        ],
        [
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 1,
                "heading": 270,
            },
            {
                "type": 2,
                "heading": 90,
            },
            {
                "type": 3,
                "heading": 180,
            },
            {
                "type": 3,
                "heading": 270,
            },
        ],
        [
            {
                "type": 3,
                "heading": 180,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 90,
            },
        ],
        [
            {
                "type": 3,
                "heading": 180,
            },
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 3,
                "heading": 270,
            },
        ],
        [
            {
                "type": 1,
                "heading": 90, 
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 270,
            },
        ],
    ],
    "level4":[
        [
            {
                "type": 1,
                "heading":0,
            },
            {
                "type": 1,
                "heading": 180,
            },
            {
                "type":1,
                "heading": 90,
            },
            {
                "type": 1,
                "heading":180,
            },
            {
                "type": 1,
                "heading":90,
            },
        ],
        [
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 270,
            },
        ],
        [
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 270,
            },
        ],
        [
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 3,
                "heading": 180,
            },
        ],
        [
            {
                "type": 1,
                "heading": 90, 
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 270,
            },
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 90,
            },
        ],
    ],
        "level5":[
        [
            {
                "type": 3,
                "heading":270,
            },
            {
                "type": 2,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 180,
            },
        ],
        [
            {
                "type": 3,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 1,
                "heading": 270,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 270,
            },
        ],
        [
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 270,
            },
        ],
        [
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 270,
            },
            {
                "type": 1,
                "heading": 0,
            },
        ],
        [
            {
                "type": 1,
                "heading": 0, 
            },
            {
                "type": 3,
                "heading": 180,
            },
            {
                "type": 3,
                "heading": 180,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 90,
            },
        ],
    ],
        "level6":[
        [
            {
                "type": 1,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 90,
            },
            {
                "type": 3,
                "heading": 180,
            },
            {
                "type": 1,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 0,
            },
        ],
        [
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 4,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 2,
                "heading": 90,
            },
        ],
        [
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 90,
            },
        ],
        [
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 2,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 0,
            },
            {
                "type": 2,
                "heading": 0,
            },
        ],
        [
            {
                "type": 1,
                "heading": 180, 
            },
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 270,
            },
            {
                "type": 1,
                "heading": 270,
            },
        ],
    ],
            "level7":[
        [
            {
                "type": 1,
                "heading": 180,
            },
            {
                "type": 1,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 1,
                "heading": 180,
            },
        ],
        [
            {
                "type": 3,
                "heading": 270,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 1,
                "heading": 180,
            },
        ],
        [
            {
                "type": 3,
                "heading": 90,
            },
            {
                "type": 3,
                "heading": 0,
            },
            {
                "type": 3,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 270,
            },
            {
                "type": 3,
                "heading": 90,
            },
        ],
        [
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 2,
                "heading": 0,
            },
            {
                "type": 4,
                "heading": 180,
            },
            {
                "type": 4,
                "heading": 0,
            },
            {
                "type": 2,
                "heading": 90,
            },
        ],
        [
            {
                "type": 3,
                "heading": 270, 
            },
            {
                "type": 1,
                "heading": 270,
            },
            {
                "type": 1,
                "heading": 90,
            },
            {
                "type": 1,
                "heading": 180,
            },
            {
                "type": 1,
                "heading": 270,
            },
        ],
    ],

}
