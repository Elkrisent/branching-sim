import random
import networkx as nx
import matplotlib.pyplot as plt

# ---------------- Phase 1: Simulation ----------------
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
            self.graph.add_node(node_id, event=event, turn=self.turn)
            current_turn_nodes.append(node_id)

            # Connect with previous turn nodes (branching)
            for prev in self.last_nodes:
                self.graph.add_edge(prev, node_id)

            self.events.append(event)
            print(event)

        self.last_nodes = current_turn_nodes
        self.turn += 1


# ---------------- Phase 2: Save & Load ----------------
def save_graph(G, filename="branching_graph.gml"):
    nx.write_gml(G, filename)

def load_graph(filename="branching_graph.gml"):
    return nx.read_gml(filename)


# ---------------- Phase 3: Visualize ----------------
def visualize_graph(G):
    # Position nodes by turn → makes timeline clearer
    pos = {}
    for node, data in G.nodes(data=True):
        turn = data.get("turn", 0)
        pos[node] = (turn, hash(node) % 10)  # x = turn, y = randomized to spread

    plt.figure(figsize=(16, 9))

    # Draw graph (nodes + edges)
    nx.draw(
        G, pos, with_labels=False,  # turn off default IDs
        node_size=1400, node_color="skyblue",
        arrows=True, alpha=0.9
    )

    # ✅ Use "event" attribute for labels
    labels = nx.get_node_attributes(G, "event")
    nx.draw_networkx_labels(G, pos, labels, font_size=9, font_color="black")

    plt.title("Branching Simulation Graph", fontsize=14)
    plt.axis("off")
    plt.show()
