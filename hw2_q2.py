from collections import namedtuple
from enum import Enum

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def improve_condition(condition):
    if condition == Condition.SICK:
        return Condition.HEALTHY
    elif condition == Condition.DYING:
        return Condition.SICK
    return condition

def worsen_condition(condition):
    if condition == Condition.SICK:
        return Condition.DYING
    elif condition == Condition.DYING:
        return Condition.DEAD
    return condition

def process_meeting(agent1, agent2):
    if agent1.category == Condition.CURE:
        if agent2.category != Condition.CURE:
            agent2 = agent2._replace(category=improve_condition(agent2.category))
    elif agent2.category == Condition.CURE:
        if agent1.category != Condition.CURE:
            agent1 = agent1._replace(category=improve_condition(agent1.category))
    else:
        agent1 = agent1._replace(category=worsen_condition(agent1.category))
        agent2 = agent2._replace(category=worsen_condition(agent2.category))
    return agent1, agent2

def filter_agents(agent_listing):
    return [agent for agent in agent_listing if agent.category not in (Condition.HEALTHY, Condition.DEAD)]

def meetup(agent_listing: tuple) -> list:
    active_agents = filter_agents(agent_listing)
    updated_agents = []
    
    it = iter(active_agents)
    for agent1, agent2 in zip(it, it):
        updated_agent1, updated_agent2 = process_meeting(agent1, agent2)
        updated_agents.extend([updated_agent1, updated_agent2])
    
    if len(active_agents) % 2 != 0:
        updated_agents.append(active_agents[-1])
    
    return updated_agents

# Example usage
agents = (
    Agent(name="A1", category=Condition.SICK),
    Agent(name="A2", category=Condition.DYING),
    Agent(name="A3", category=Condition.HEALTHY),
    Agent(name="A4", category=Condition.CURE),
    Agent(name="A5", category=Condition.SICK),
)

updated_agents = meetup(agents)
for agent in updated_agents:
    print(f"Name: {agent.name}, Category: {agent.category}")

