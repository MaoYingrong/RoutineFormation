import mesa
import random


class ActorAgent(mesa.Agent):
    """
    Individual Agent definition and its properties/interaction methods
    """

    def __init__(
        self,
        unique_id,
        model,
        prob_memory,
        availablity
    ):
        super().__init__(unique_id, model)
        self.memory = {}
        self.skills_set = []
        self.prob_memory = prob_memory
        self.aviablity = availablity
        self.parent = None
        self.explored = False
    

    def have_skill(self, task):
        return task in self.skills_set
    

    def know_others(self, task):
        try:
            actors_lst = self.memory[task]
            return True, random.choice(actors_lst)
        except KeyError:
            return False, None
        

    def update_memory(self, task, agent, prob_memory):
        if self.model.random.random() < prob_memory:
            try:
                self.memory[task].append(agent)
            except KeyError:
                self.memory[task] = [agent]


    def update_all_memory(self, task):
        working_agent = self
        agent = self.parent
        while agent:
            agent.update_memory(task, working_agent, self.prob_memory)
            agent = agent.parent


    def available(self):
        return self.model.random.random() < self.aviablity


    def step(self, task):
        """Actors' decision-making process"""
        task = self.model.tasks_lst[0]
        know_others, actor = self.know_others(task)

        if not self.have_skill(task) and not know_others:
            return False, self.model.grid.get_neighbors(
                self.pos, include_center=False
                )
        
        if self.have_skill(task):
            working_agent = self
        elif know_others:
            working_agent = actor

        return True, [working_agent]


        

