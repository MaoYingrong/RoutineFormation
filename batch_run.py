from routine_formation.model import OrgNetwork
from mesa import batch_run
import pandas as pd 
import numpy as np


parameters = {
    "num_tasks": 8,  
    "num_nodes": range(10, 101, 10),
    "num_new_edges": range(1, 9, 1),
    "skills_ratio": 0.1,
    "prob_memory": 0.6,
    "availablity": 0.7
}

results = batch_run(OrgNetwork,
                    parameters,
                    iterations=10,
                    max_steps=50, #Here the steps means the number of problem instead of really model steps.
                    data_collection_period=-1)

pd.DataFrame(results).to_csv("./batch_data.csv")