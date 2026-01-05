import pandas as pd
import numpy as np

equipment_master = pd.DataFrame({
    'equipment_id': ['P001', 'P002', 'T001', 'T002'],
    'equipment_name': ['Main Feed Pump', 'Backup Pump', 'Reactor Tank', 'Storage Tank'],
    'installation_date': pd.to_datetime(['2020-01-15', '2020-02-01', '2019-06-10', '2019-07-20']),
    'manufacturer': ['Grundfos', 'Grundfos', 'Pfaudler', 'Pfaudler']
})

print(equipment_master)

maintenance_records = pd.DataFrame({
    'equipment_id': ['P001', 'P001', 'P002', 'T001', 'T002'],
    'maintenance_date': pd.to_datetime(['2024-01-15', '2024-02-20', '2024-01-20', '2024-02-10', '2024-03-05']),
    'maintenance_type': ['Preventive', 'Corrective', 'Preventive', 'Inspection', 'Preventive'],
    'cost': [1500, 2500, 1200, 800, 1800],
    'duration_hours': [4, 8, 3, 2, 6]
})

print(maintenance_records)

equipment_maintenance = pd.merge(equipment_master, maintenance_records, 
                                on='equipment_id', how='left')

print(equipment_maintenance)