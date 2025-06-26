from mysql.connector import connect, Error
from models.agent import Agent, Status

class AgentDal:
    def __init__(self, host='localhost', database='eagleEyeDB',user='root', password=''):
        try:
            self.conn = connect(host=host, database=database, user=user, password=password)
            self.cursor = self.conn.cursor()
            print("Connected to MySQL successfully.")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.conn = None
            self.cursor = None

    def add_agent(self, agent:Agent):
        sql ="""
        INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
        VALUES(%s, %s, %s, %s, %s)
        """
        values = (agent.code_name, agent.real_name, agent.location, agent.status.value, agent.missions_completed)
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Agent added successfully.")
        except Error as e:
            print(f"Failed to add agent: {e}")


    def get_all_agents(self):
        sql = "SELECT id, codeName, realName, location, status, missionCompleted FROM agents"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fatchall()
            agents = []
            for row in results:
                agent = Agent(
                    code_name=row[1],
                    real_name=row[2],
                    location=row[3],
                    status=Status(row[4]),
                    missions_completed=row[5],
                    agent_id=row[0]
                )
                agents.append(agent)
            return  agents
        except Error as e:
            print(f"Failed to fetch agents: {e}")
            return []

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("MySql connection closed.")
