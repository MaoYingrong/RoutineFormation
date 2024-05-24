# Routine_Formation

## Summary  
This model simulates how network structures impact the formation and change of organizational routines.  

When an organization confronts a problem that can be divided into multiple tasks, since each individual actor possesses different skills, each task can only be completed by certain actors, while initially, no one has this information. After confronting the same problem several times, the organization would form a routine of which actor performs which task. This routine is relatively stable, but owing to the difference in search order and actors’ availability, there may also be some variation. In the simulation, we can observe that when the problems occur more, the time used to solve one problem decreases because of the decrease in the search time. 

## How to Run

To run the model interactively, run ``run.py`` in this directory. e.g.

```
    $ python run.py
```

## Files

* ``model.py``: Core model code.
* ``agent.py``: Core agent code.
* ``server.py``: Sets up the interactive visualization.
* ``batch_run.ipynb``: Jupyter notebook conducting some preliminary analysis of the model.

## Reference

This model is based adapted from:

Miller, K. D., Choi, S., & Pentland, B. T. (2014). The role of transactive memory in the formation of organizational routines. Strategic Organization, 12(2), 109-133.  

