import openai
openai.api_key = 'use real key here'

def comp(PROMPT, MaxToken=50,outputs=1):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt = PROMPT + ".Give a fun fact about mushrooms that relates to this question.",
        max_tokens = MaxToken,
        n = outputs
    )
    output = list()
    for k in response['choices']:
        output.append(k['text'].strip())
    return output


def comp2(PROMPT, MaxToken=50,outputs=1):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt = PROMPT,
        max_tokens = MaxToken,
        n = outputs
    )
    output = list()
    for k in response['choices']:
        output.append(k['text'].strip())
    return output

def mushroom(input):
    PROMPT = input
    PROMPT = PROMPT.capitalize()
    check = PROMPT.find("Mushroom")

    if check == -1:
        check = PROMPT.find("mushroom")
        if check == -1:
            return comp(PROMPT,MaxToken=300,outputs = 1)
        else:
            return comp2(PROMPT,MaxToken=300,outputs = 1)
    else:
        return comp2(PROMPT,MaxToken=300,outputs = 1)
"""
print("Hello World I am Mbot, your mushroom loving companion")
while True:
    enter = input("Please ask a question below and I will do my best to answer:\n")
    if enter == "quit":
        print("Goodbye")
        break
    else:
        print(mushroom(enter))
"""