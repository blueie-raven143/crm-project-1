import numpy as np
import pandas as pd
np.random.seed(42)
phoneno=[''.join(np.random.choice(list('1234567890'),10))for _ in range(50)]
alpha=list('adcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
name =[''.join(np.random.choice(alpha,10))for _ in range(50)]
df=pd.DataFrame({
    "Names": name,
    "Phone Numbers": phoneno
})
df.to_csv("support_leads.csv", index=False)