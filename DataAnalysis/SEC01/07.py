import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

day = np.array([1, 2, 3, 4, 5, 6, 7])
china = np.array([13, 14, 17, 13, 18, 16, 12])
usa = np.array([14, 16, 21, 29, 24, 14, 8])

plt.plot(day, china, label="China", color='red', marker="p", linestyle="--")
plt.scatter(day, usa, label="USA", color='blue', marker="o")
plt.title("Covid Death")
plt.grid()
plt.xlabel("Day")
plt.ylabel("Covid Death")
plt.legend()
plt.show()

df = pd.DataFrame(np.c_[day, china, usa], columns=['day', 'china', 'usa'])
# print(df)

df.to_csv("Covid Death.csv", index=False)