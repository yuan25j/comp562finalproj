import pandas as pd
initial_df = pd.read_csv('Collisions.csv') # All attributes
# Declaring needed columns
df = pd.DataFrame()
wanted_columns = ['X', 'Y', 'ADDRTYPE','SEVERITYCODE', 'VEHCOUNT', 'INJURIES', 'SERIOUSINJURIES',
                 'FATALITIES', 'JUNCTIONTYPE', 'UNDERINFL', 'WEATHER', 'ROADCOND', 'LIGHTCOND']
# Constructing new dataset with only those necessary
for c in wanted_columns:
        df[str(c)] = initial_df[c]


df.to_csv("SelectedCollisionCols.csv", index=False)