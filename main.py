from engine import Agent, Environment, save_graph, load_graph, visualize_graph
import networkx as nx

# Step 1: Create agents
agents = [
    Agent("Hero", health=12, strength=4),
    Agent("Bandit", health=10, strength=3),
    Agent("NPC", health=8, strength=2)
]

# Step 2: Create environment
env = Environment(agents)

# Step 3: Run 5 turns of simulation
for _ in range(5):
    print(f"\n--- Turn {env.turn} ---")
    env.run_turn()

# Step 4: Print final agent states
print("\nFinal states:")
for a in agents:
    print(a)

# Step 5: Save, reload, and visualize the simulation graph
save_graph(env.graph, "branching_graph.gml")
print("\nBranching graph saved as branching_graph.gml")

G_loaded = load_graph("branching_graph.gml")
visualize_graph(G_loaded)
