import hashlib
import random
import requests

class AgentHandler:
    def __init__(self, SCRAPEOPS_API_KEY='57d5f60f-fbbe-49c3-8e54-c9d41b7a6475'):
        self.SCRAPEOPS_API_KEY = SCRAPEOPS_API_KEY
        self.hash_object = hashlib.sha256()
        self.agent_dict = {}
        self.agent_history = {}
        self.generate_user_agents()
        return


    def generate_user_agents(self, num=100):
        # Pulls list of 100 user agents from scapeops user-agent api
        response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=' + self.SCRAPEOPS_API_KEY + '&num_results=' + str(num))
        json_response = response.json()
        agents_list = json_response.get('result', [])
        self.generate_agents_hash(agents_list)
        return 


    def generate_agents_hash(self, agents_list):
        for s in agents_list:
            # Update the hash object with the bytes of the string
            self.hash_object.update(s.encode('utf-8'))
            
            # Get the hexadecimal representation of the hash
            hex_dig = self.hash_object.hexdigest()
            
            # Convert the hexadecimal hash to an integer
            hash_number = int(hex_dig, 16)

            # Ensures same user agent hasn't been pulled in the past 
            if hash_number not in self.agent_dict.keys() and hash_number not in self.agent_history.keys():
                self.agent_dict[hash_number] = s
            else:
                raise Exception('User Agent has been used in the past')
        return


    def get_agent(self):
        # Choose random user agent
        agent_flag = False

        # If current list of user agents has been exhausted, call API and generate new list
        if len(self.agent_dict) == 0:
            self.generate_user_agents()

        hash_number, user_agent = random.choice(list(self.agent_dict.items()))

        # Check to ensure user_agent hasn't been used before
        if hash_number in self.agent_history:
            raise Exception('User agent has been used in the past')
        else:
            self.agent_history[hash_number] = user_agent
            self.agent_dict.pop(hash_number)

        return user_agent
            



                





