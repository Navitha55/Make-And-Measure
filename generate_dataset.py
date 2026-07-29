import pandas as pd
import random
import numpy as np

fabrics = {
    'Cotton': 100,
    'Silk': 180,
    'Velvet': 200,
    'Organza': 170,
    'Lenin': 120,
    'Polyster': 90
}

dress_types = {
    'Short Kurtis': 150,
    'Punjabi Suits': 180,
    'Tunics': 180,
    'Saree': 180,
    'Skirt': 190,
    'Frock': 130
}

def generate_body_measurements():
    height = random.randint(140, 180)
    weight = random.randint(40, 80)
    chest = random.randint(70, 110)
    waist = random.randint(60, 100)
    hips = random.randint(75, 110)
    shoulders = random.randint(35, 50)
    arm_length = random.randint(45, 65)
    return height, weight, chest, waist, hips, shoulders, arm_length

def calculate_stitching_cost(fabric, dress_type, height, weight, chest, waist, hips, shoulders, arm_length):
    fabric_cost = fabrics[fabric]
    dress_cost = dress_types[dress_type]
    body_area = chest + waist + hips + shoulders + arm_length + (height * 0.5) + (weight * 0.2)
    stitching_rate = 1.5
    return int(fabric_cost + dress_cost + (body_area * stitching_rate))

data = []
for _ in range(1000):
    fabric = random.choice(list(fabrics.keys()))
    dress_type = random.choice(list(dress_types.keys()))
    height, weight, chest, waist, hips, shoulders, arm_length = generate_body_measurements()
    cost = calculate_stitching_cost(fabric, dress_type, height, weight, chest, waist, hips, shoulders, arm_length)
    
    data.append({
        'height': round(height, 1),
        'weight': round(weight, 1),
        'chest': round(chest, 1),
        'waist': round(waist, 1),
        'hips': round(hips, 1),
        'shoulders': round(shoulders, 1),
        'arm_length': round(arm_length, 1),
        'fabric': fabric,
        'dress_type': dress_type,
        'stitching_cost': cost
    })

df = pd.DataFrame(data)
df.to_csv('synthetic_stitching_data.csv', index=False)
