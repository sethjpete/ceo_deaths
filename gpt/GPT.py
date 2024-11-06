from config import API_KEY as key
from config import ORGANIZATION as org

import openai

class GPT:
    """
    Singleton class for GPT-3 API

    TODO: Should this be a singleton?
    """

    instance = None
    model_type = None
    conversation_history = []
    system_prompts = []
    max_tokens = 100
    temperature = 0.8

    def __new__(cls):
        if cls.instance is None:
            print('Instance does not exist')
            print('Creating openai instance')
            print('Key: ' + key)
            print('Org: ' + org)

            openai.organization = org
            openai.api_key = key
            cls.instance = super().__new__(cls)

        print('Instance exists')
        return cls.instance
    
    def __init__(self, model_type = 'gpt-3.5-turbo', system_prompts = [], max_tokens = 100, temperature = 0.8):
        self.model_type = model_type
        self.system_prompts = system_prompts
        self.max_tokens = max_tokens
        self.temperature = temperature
        print("Initializing GPT, model type: " + model_type)
    
    def add_system_prompt(self, prompt):
        prompt_dict = {'role': 'system', 'content': prompt + '\n'}
        self.system_prompts.append(prompt_dict)
        print("Added system prompt: " + prompt)

    def reset_conversation_history(self):
        self.conversation_history = []
        print("Reset conversation history")

    def reset_system_prompts(self):
        self.system_prompts = []
        print("Reset system prompts")

    def edit_max_tokens(self, max_tokens):
        self.max_tokens = max_tokens
        print("Max tokens set to: " + str(max_tokens))
    
    def query(self, query):
        print("Querying GPT")
        response = openai.ChatCompletion.create(
            model=self.model_type,
            messages = self.conversation_history + self.system_prompts + 
            [{
                'role': 'user',
                'content': query
            }],
            max_tokens=100,
            temperature=self.temperature
        )

        self.conversation_history.append({
            'role': 'user',
            'content': query
        })
        
        print('Token use: ' + str(response["usage"]["total_tokens"]))
        return response['choices'][0]['message']['content']