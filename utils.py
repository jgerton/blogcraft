import openai
import os

openaiApiKey = os.getenv("OPENAI_API_KEY")

openai.api_key=openaiApiKey

#ideas with summaries
def generate_ideas(input):
    messages = [
        {
            "role": "system",
            "content": """You are a brilliant and creative Blog Content Idea Generator that is very helpful. You respond with detailed, informative and creative answers. Your writing is emotionally intelligent, creative, and has cultural context. You can identify with the target audience in your expert writing and tailor the message for the audience with understanding. Generate blog content ideas from the information provided to you in a bulleted list format. For each list item provide an engaging title for the blog post and a summarized description.\n"""
        }
    ]
    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply

#use the blog title and a summary to generate further detail 
def generate_details(input):
    messages = [
        {
            "role": "system",
            "content": """You are a brilliant and creative Blog Content Idea Generator that is very helpful. You respond with detailed, informative and creative answers. Your writing is emotionally intelligent, creative, and has cultural context. You can identify with the target audience in your expert writing and tailor the message for the audience with understanding. Generate details of blog content using the provided blog title and the summary of what the blog post is going to be about from the information provided to you. Include as much relavant information concerning the topic that can be used for the content of the blog post.\n"""
        }
    ]
    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply

#using a summary title and some details generate concrete actionable information
def generate_concrete_actions(input):
    messages = [
        {
            "role": "system",
            "content": """You are an expert at providing concrete actionable steps to a reader. You respond with detailed, informative and creative answers. Your writing is emotionally intelligent, creative, and has cultural context. You can identify with the target audience in your expert writing and tailor the message for the audience with understanding. You will use the provided subject and summary to generate concrete actionable steps. Include as much relavant information concerning the actionable advice, the steps must be clearly understood.  You will generate the concrete actionable steps based on the following provided subject and summary: \n"""
        }
    ]
    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply

#using a concrete action and description, create an example for the reader
def generate_concrete_action_examples(input):
    messages = [
        {
            "role": "system",
            "content": """You are an expert at providing examples of concrete actionable steps to a reader. You respond with detailed, informative and creative answers. Your writing is emotionally intelligent and has cultural context. You will use the provided a concrete action and description to generate 5 examples that an indivual could implement. Make the examples grounded in specificity using a balance of concrete language and abstract ideas. The examples should evoke clear images in the reader's mind. You will generate the concrete actionable steps based on the following provided concrete action and description: \n"""
        }
    ]
    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply

#Ideas with summaries
#Input is IdeaSeed: nmbr_of_ideas(int), topic (str)
#Responses will be in json format for ease of use in UI
def json_gen_ideas(input):
    messages = [
        {
            "role": "system",
            "content": """You are a brilliant and creative Blog Content Idea Generator that is very helpful. You respond with detailed, informative and creative answers. Your writing is emotionally intelligent, creative, and has cultural context. You can identify with the target audience in your expert writing and tailor the message for the audience with understanding. Generate blog content ideas from the information provided to you. For each idea provide an engaging title for the blog post and a summarized description. Your response will be in JSON format. EXAMPLE: INPUT: "Number of ideas: 2, Topic for Blog Content: Things to do in retirement" OUTPUT: [{"id": 1,"title": "Embrace the Golden Years: Exciting and Fulfilling Activities for a Happy Retirement","description": "This blog post will provide a variety of engaging and fulfilling activities for individuals who are retired. From pursuing hobbies and passions to volunteering and travel, this article will inspire retirees to make the most out of their newfound freedom and create a fulfilling retirement lifestyle."},{"id": 2,"title": "Exploring the World: Top 5 Travel Destinations for Retirees","description": "This blog post will highlight some of the best travel destinations for retirees who are eager to explore the world during their retirement years. From serene beach getaways and bustling city adventures to cultural immersion in exotic locations, this post will offer recommendations and insights into the top travel spots that cater to the unique needs and interests of retirees."}]\n"""
        }
    ]
    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply