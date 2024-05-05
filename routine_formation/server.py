import math

import mesa

from .model import OrgNetwork


def network_portrayal(G):
    # The model ensures there is always 1 agent per node

    def node_color(agent):
        if len(agent.memory) == 0:
            color = "#F5B7B1"
        elif len(agent.memory) == 1:
            color = "#F1948A"
        elif len(agent.memory) == 2:
            color = "#E74C3C"
        elif len(agent.memory) == 3:
            color = "#B03A2E"
        else:
            color = "#78281F"
        return color


    portrayal = {}
    portrayal["nodes"] = [
        {
            "size": 6,
            "color": node_color(agents[0]),
            "tooltip": f"id:{agents[0].pos}<br>memory: {agents[0].memory}",
            "label": f"{agents[0].unique_id}",

        }
        for (_, agents) in G.nodes.data("agent")
    ]

    portrayal["edges"] = [
        {
            "source": source,
            "target": target,
            "color": "#566573",
            "width": 1,
        }
        for (source, target) in G.edges
    ]

    return portrayal

def txt_description(model):
    result = []
    for i in model.searching_list:
        result.append(i.unique_id)
    return f"The present status: {model.status}\
        <br>Current task: {model.tasks_lst[0]}\
        <br>Searching list: {str(result)}\
        <br>Current routine: {model.routine}\
        <br><br>Routine list: {model.routine_lst}"



network = mesa.visualization.NetworkModule(
    portrayal_method=network_portrayal,
    canvas_height=500,
    canvas_width=500,
)


chart = mesa.visualization.ChartModule(
    [
        {"Label": "Time", "Color": "#0000FF"},
    ]
)

model_params = {
    "num_nodes": mesa.visualization.Slider(
        name="Number of agents", 
        min_value=10, 
        max_value=100, 
        step=10, 
        value=20
    ),
    "num_new_edges": mesa.visualization.Slider(
        name="Number of edges to attach <br>from a new node to existing nodes", 
        min_value=1, 
        max_value=10, 
        step=1, 
        value=3
    ),
    "num_tasks": mesa.visualization.Slider(
        name="Number of tasks", 
        min_value=2, 
        max_value=20, 
        step=1, 
        value=8
    ),
    "skills_proportion": mesa.visualization.Slider(
        name="Skills ratio", 
        min_value=0.1, 
        max_value=0.5, 
        step=0.05, 
        value=0.1
    ),
    "prob_memory": mesa.visualization.Slider(
        name="Probability of memory", 
        min_value=0, 
        max_value=1, 
        step=0.1, 
        value=0.6
    ),
    "availablity": mesa.visualization.Slider(
        name="Availablity", 
        min_value=0, 
        max_value=1, 
        step=0.1, 
        value=0.5
    ),
}

server = mesa.visualization.ModularServer(
    model_cls=OrgNetwork,
    visualization_elements=[network, txt_description, chart],
    name="Routine Formation Model",
    model_params=model_params,
)
server.port = 8521
