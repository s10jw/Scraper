import hashlib
from random
import requests

class AgentHandler:
    def __init__(self, SCRAPEOPS_API_KEY='57d5f60f-fbbe-49c3-8e54-c9d41b7a6475'):
        self.SCRAPEOPS_API_KEY
        self.hash_object = hashlib.sha256()
        self.agent_dict = {}
        self.agent_history = {}
        return


    def get_user_agents(self, num=100):
        response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=' + self.SCRAPEOPS_API_KEY + '&num_results=' + str(num))
        json_response = response.json()
        agents_list = json_response.get('result', [])
        generate_agents_hash(agents_list)
        return 


    def generate_agents_hash(self, agents_list):
        for s in agents_list:
            # Update the hash object with the bytes of the string
            self.hash_object.update(s.encode('utf-8'))
            
            # Get the hexadecimal representation of the hash
            hex_dig = hash_object.hexdigest()
            
            # Convert the hexadecimal hash to an integer
            hash_number = int(hex_dig, 16)

            # Ensures user agent hasn't been pulled in the past 
            if hash_number not in self.agent_dict.keys():
                self.agent_dict[hash_number] = s
                else:
                    raise Exception('User Agent already exists in agent_dict')
        return


        def get_agent(self):
            # Choose random user agent
            agent_flag = False
            hash_number, user_agent = random.choice(list(self.agent_dict.items()))

            # Check to ensure user_agent hasn't been used before
            if hash_number in self.agent_history:
                raise Exception('User agent has already been used in session')
                else:
                    self.agent_history.add(hash_number)

            return user_agent
            



                





