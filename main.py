from models.agent import Agent, Status
from DAL.agent_dal import AgentDal

def display_menu():
    print("\nAgent Management System")
    print("1. Add agent")
    print("2. View all agents")
    print("3. Exit")

def add_agent(dal: AgentDal):
    print("\nadd new agent: ")
    code = input("Code name: ")
    real = input("Real name: ")
    loc = input("Location: ")
    print("Available statuses:")
    for s in Status:
        print(f"-{s.value}")
    status_input = input("Enter status: ").capitalize()
    if status_input not in [s.value for s in Status]:
        print("Invalid status. Defaulting to 'Active'")
        status = Status.ACTIVE
    else:
        status = Status(status_input)

    try:
        mission = int(input("Mission completed: "))
    except ValueError:
        print("Invalid number, setting missions to 0")
        mission =  0

    agent = Agent(code, real, status, loc, mission)
    dal.add_agent(agent)

def view_all_agents(dal:AgentDal):
    print("\n All Agents:")
    agents = dal.get_all_agents()
    if not agents:
        print("No agents found")
    else:
        for a in agents:
            print(a)

def main():
    dal = AgentDal()
    while True:
        display_menu()
        choice = input("Choose an option: ")

        match choice:
            case "1":
                add_agent(dal)
            case "2":
                view_all_agents(dal)
            case "3":
                dal.close()
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Try again")


main()