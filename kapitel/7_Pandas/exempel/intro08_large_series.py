import pandas as pd
import numpy as np
import sys

equipment_ids = ['Pump_001', 'Motor_002', 'Tank_003', 'Compressor_004', 'Valve_005']

large_series_idx = np.random.choice(equipment_ids, size=20)
temperatures = pd.Series(np.random.uniform(70, 90, size=20), index=large_series_idx)
pressures = pd.Series(np.random.uniform(0.5, 10, size=20), index=large_series_idx)
vibrations = pd.Series(np.random.uniform(0.1, 3, size=20), index=large_series_idx)

equipment_df = pd.DataFrame({
    'temperature_c': temperatures,
    'pressure_bar': pressures,
    'vibration_mm_s': vibrations
})

print(equipment_df)
print(equipment_df.sort_index())

grouped_df = equipment_df.groupby(equipment_df.index).mean()
print(grouped_df)   

pressure_max_df = equipment_df.groupby(equipment_df.index)['pressure_bar'].max()
print(pressure_max_df)

agg_df = equipment_df.groupby(equipment_df.index).agg(['mean', 'std'])
print(agg_df)