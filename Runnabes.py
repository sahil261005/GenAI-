import random

class NakliLLM:

  def __init__(self):
    print('LLM created')

  def predict(self, prompt):

    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}



class NakliPromptTemplate:

  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  def format(self, input_dict):
    return self.template.format(**input_dict)



template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)


prompt = template.format({'length':'short','topic':'india'})

llm = NakliLLM()

llm.predict(prompt)
