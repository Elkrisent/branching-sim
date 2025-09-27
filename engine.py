import random
import networkx as nx

class Agent:
    def __init__(self, name, health=10, strength=3):
        self.name = name
        self.health = health
        self.strength = strength

    def is_alive(self):
        return self.health > 0

    def choose_action(self, others):
        if not others:
            return ("wait", None)
        
        action = random.choice(["attack", "wait"])
        if action == "attack":
            target = random.choice(others)
            return ("attack", target)
        return ("wait", None)

    def __repr__(self):
        return f"{self.name}(HP={self.health})"

class Environment:
    def __init__(self, agents):
        self.agents = agents
        self.turn = 0
        self.events = []
        self.graph = nx.DiGraph()  # Directed graph for branching
        self.last_nodes = []  # nodes from the previous turn

    def run_turn(self):
        alive_agents = [a for a in self.agents if a.is_alive()]
        current_turn_nodes = []

        for agent in alive_agents:
            others = [a for a in alive_agents if a != agent]
            action, target = agent.choose_action(others)

            if action == "attack" and target:
                damage = random.randint(1, agent.strength)
                target.health -= damage
                event = f"{agent.name} attacked {target.name} for {damage} damage!"
            else:
                event = f"{agent.name} waits."

            # Add event to graph
            node_id = f"Turn{self.turn}_{agent.name}_{random.randint(0,1000)}"
            self.graph.add_node(node_id, label=event, turn=self.turn)
            current_turn_nodes.append(node_id)

            # Connect with previous turn nodes (branching)
            for prev in self.last_nodes:
                self.graph.add_edge(prev, node_id)

            self.events.append(event)
            print(event)

        self.last_nodes = current_turn_nodes
        self.turn += 1
