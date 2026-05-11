"""Agno Basic Agent - Hello World"""
from agno.agent import Agent

agent = Agent(
    name="Hetzy-Test",
    model="openai:gpt-4o-mini",
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response("¿Cuál es la capital de Francia? Responde en una frase.")