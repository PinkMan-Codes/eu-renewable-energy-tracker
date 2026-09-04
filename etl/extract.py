import eurostat
import pandas as pd


sdg = eurostat.get_data_df("sdg_07_40")
env_air = eurostat.get_data_df("env_air_gge")
pop = eurostat.get_data_df("demo_pjan")

#file save
sdg.to_csv("data/raw/sdg_07_40.csv", index=False)
env_air.to_csv("data/raw/env_air_.csv", index=False)
pop.to_csv("data/raw/pop.csv", index=False)