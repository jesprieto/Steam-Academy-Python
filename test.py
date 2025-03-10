#import pandas as pd
#print(pd.__version__)
from tabulate import tabulate
import pandas as pd

df = pd.read_csv("DB1.csv")

# Mostrar los datos en formato tabla
print(tabulate(df, headers="keys", tablefmt="grid"))

