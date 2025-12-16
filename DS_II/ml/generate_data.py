import pandas as pd
import random

data = []

for i in range(1000):
    if random.random() < 0.1:  # fake data
        temp = random.uniform(80, 120)
        hum = random.uniform(0, 20)
        label = -1
    else:
        temp = random.uniform(20, 35)
        hum = random.uniform(40, 70)
        label = 1

    data.append([temp, hum, label])

df = pd.DataFrame(data, columns=["temperature", "humidity", "label"])
df.to_csv("../data/sensor_data.csv", index=False)

print("Dataset created")
