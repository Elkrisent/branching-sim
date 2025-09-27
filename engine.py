import random

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

    def run_turn(self):
        alive_agents = [a for a in self.agents if a.is_alive()]
        for agent in alive_agents:
            others = [a for a in alive_agents if a != agent]
            action, target = agent.choose_action(others)

            if action == "attack" and target:
                damage = random.randint(1, agent.strength)
                target.health -= damage
                event = f"{agent.name} attacked {target.name} for {damage} damage!"
            else:
                event = f"{agent.name} waits."

            self.events.append(event)
            print(event)

        self.turn += 1
