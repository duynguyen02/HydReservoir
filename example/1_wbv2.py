import pandas as pd

from hydreservoir.water_balance.v2.hydraulic_component import BoxCulvert
from hydreservoir.water_balance.v2.hydraulic_component import CircularCulvert
from hydreservoir.water_balance.v2.hydraulic_component import CircularCulvertV2
from hydreservoir.water_balance.v2.hydraulic_component import FreeSpillway
from hydreservoir.water_balance.v2.hydraulic_component import Pump
from hydreservoir.water_balance.v2.hydraulic_component.simple.unknown import Unknown
from hydreservoir.water_balance.v2.hydraulic_component.spillway.gated_spillway import GatedSpillway
from hydreservoir.water_balance.v2.wb import WB

df = pd.read_csv('data.csv')

free_spillway = FreeSpillway(
    'FS1', 109.3, 19.0
)

gated_spillway = GatedSpillway(
    'GS1', 109.3, 19.0,
    df['GatedA'].to_numpy(), free_spillway
)

circular_culvert = CircularCulvert(
    'CC1', 102.5, 0.4, df['CircularA'].to_numpy(), free_spillway,
    discharge_coefficient=0.9, contraction_coefficient=1.0
)

circular_culvert_v2 = CircularCulvertV2(
    'CC2', 102.5, 0.4, df['CircularA'].to_numpy(), free_spillway,
    discharge_coefficient=0.9, contraction_coefficient=1.0
)

box_culvert = BoxCulvert(
    'BC1', 102.5, 0.4, df['BoxA'].to_numpy(), free_spillway
)

pump = Pump(
    'P1', df['P'].to_numpy()
)

unknown = Unknown(
    'U1', df['P'].to_numpy()
)

timeseries = pd.to_datetime(df['Timeseries'])

wb = WB(
    timeseries.to_numpy(),
    df['WaterLevel'].astype(float).to_numpy(),
    df['Capacity'].astype(float).to_numpy(),
)

(
    wb.add_component(free_spillway).add_component(gated_spillway)
    .add_component(circular_culvert).add_component(circular_culvert_v2)
    .add_component(box_culvert).add_component(pump).add_component(unknown)
)
wb.calculate().to_csv('result.csv', index=False)
