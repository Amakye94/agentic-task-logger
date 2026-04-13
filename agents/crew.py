from crewai import Agent, Task, Crew

def run_agents():

    coder = Agent(
        role="Developer",
        goal="Generate a short task description",
        backstory="Expert coder",
        llm="ollama/llama3"
    )

    task = Task(
        description="Generate a short task like 'Study for 2 hours'",
        expected_output="Short task text",
        agent=coder
    )

    crew = Crew(
        agents=[coder],
        tasks=[task]
    )

    result = crew.kickoff()
    return str(result)