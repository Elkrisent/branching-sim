from engine import Agent, Environment

# Create agents
agents = [
    Agent("Hero", health=12, strength=4),
    Agent("Bandit", health=10, strength=3),
    Agent("NPC", health=8, strength=2)
]

env = Environment(agents)

# Run 5 turns
for _ in range(5):
    print(f"\n--- Turn {env.turn} ---")
    env.run_turn()

print("\nFinal states:")
for a in agents:
    print(a)
