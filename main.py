from models.agent import Agent, Status
from DAL.agent_dal import AgentDal

def display_menu():
    print("\nAgent Management System")
    print("1. Add agent")
    print("2. View all agents")
    print("3. Update Agent")
    print("4. Delete Agent")
    print("5. Exit")

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

def update_agent_flow(dal: AgentDal):
    try:
        agent_id = int(input("Enter agent ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
    print("Enter new details:")
    code = input("New code name: ")
    real = input("New real name: ")
    loc = input("New location: ")

    print("Available statuses:")
    for s in Status:
        print(f"- {s.value}")
    status_input = input("Enter new status: ").capitalize()
    if status_input not in [s.value for s in Status]:
        print("Invalid status. Using 'Active'")
        status = Status.ACTIVE
    else:
        status = Status(status_input)

    try:
        missions = int(input("New number of missions completed: "))
    except ValueError:
        print("Invalid number. Using 0.")
        missions = 0

    agent = Agent(code, real, loc, status, missions, agent_id=agent_id)
    dal.update_agent(agent)

def delete_agent_flow(dal: AgentDal):
    try:
        agent_id = int(input("Enter agent ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    confirm = input(f"Are you sure you want to delete agent {agent_id}? (y/n): ").lower()
    if confirm == "y":
        dal.delete_agent(agent_id)
    else:
        print("Deletion cancelled.")


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
                update_agent_flow(dal)
            case "4":
                delete_agent_flow(dal)
            case "5":
                dal.close()
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Try again")


main()