materials = {
    "Iridium": {
        "Overheat_Temp": "1500",
        "Cooldown_Time": "9",
    },
    "Cobalt": {
        "Overheat_Temp": "1640",
        "Cooldown_Time": "8",
    },
    "Chromium": {
        "Overheat_Temp": "1785",
        "Cooldown_Time": "14",
    },
    "Titanium": {
        "Overheat_Temp": "1835",
        "Cooldown_Time": "11",
    },
    "Steel": {
        "Overheat_Temp": "1890",
        "Cooldown_Time": "17",
    },
    "Iron": {
        "Overheat_Temp": "2100",
        "Cooldown_Time": "22",
    },
    "Tungsten": {
        "Overheat_Temp": "2175",
        "Cooldown_Time": "20",
    },
    "Diamond": {
        "Overheat_Temp": "2500",
        "Cooldown_Time": "60",
    }
}

Numbers = {}

from math import floor
from json import dump

for material in materials:
    Material_Numbers = {}
    for speed in range(1,400):
        speed = float(speed)
        Overheat_Time = 1.4**(float(materials[material].get('Overheat_Temp'))/speed)
        Total_Digging = float(866142/(6*speed))
        Total_Cycles = Total_Digging/Overheat_Time
        Complete_Cycles = floor(Total_Cycles)
        Total_Cooldown = float(materials[material].get('Cooldown_Time')) * Complete_Cycles
        Total_Time = Total_Cooldown + Total_Digging
        if Total_Time > 1080.0:
            break
        Material_Numbers[Total_Time] = speed
    Numbers[material] = Material_Numbers
    print(f'Best result from \u001b[35m{material}\u001b[0m: {min(Material_Numbers.keys())}')


with open('results.json', 'w') as f:
    dump(Numbers, f, indent=2)
