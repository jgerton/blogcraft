from pydantic import BaseModel
from fastapi import FastAPI
from utils import generate_ideas, generate_details, generate_concrete_actions, generate_concrete_action_examples, json_gen_ideas

# initialize fastapi
app = FastAPI()

# define data model
class IdeaSeed(BaseModel):
    nmbr_of_ideas: int
    topic: str

class ContentIdeaDetails(BaseModel):
    title: str
    summary: str

class ConcreteActionTopic(BaseModel):
    subject: str
    summary: str

#BaseModel: concrete action and description
class ConcreteExample(BaseModel):
    concrete_action: str
    description: str

# api routes
@app.get("/")
async def root():
    return {"message": "http://yourLifecraft.com BlogCraft API service!!"}

@app.post("/content_ideas")
async def generate_content_ideas(ideaSeed: IdeaSeed):
    content_ideas = generate_ideas(f"Number of ideas: {ideaSeed.nmbr_of_ideas}, Topic for Blog Content: {ideaSeed.topic}.")
    return {"content_ideas": content_ideas}

#json format responses from ai
@app.post("/content_ideas_json")
async def generate_content_ideas_json(ideaSeed: IdeaSeed):
    content_ideas_json = json_gen_ideas(f"Number of ideas: {ideaSeed.nmbr_of_ideas}, Topic for Blog Content: {ideaSeed.topic}.")
    return {"content_ideas": content_ideas_json}

@app.post("/content_details")
async def generate_content_details(contentTopic: ContentIdeaDetails):
    content_details = generate_details(f"Title: {contentTopic.title}, Summary: {contentTopic.summary}.")
    return {"content_details": content_details}

#utils generate_concrete_actions
@app.post("/concrete_actions")
async def generate_actions(actionTopic: ConcreteActionTopic):
    concrete_actions = generate_concrete_actions(f"Subject: {actionTopic.subject}, Summary: {actionTopic.summary}.")
    return{"concrete_actions": concrete_actions}

#utils generate_concrete_action_examples 
#   accepts (BaseModel) ConcreteExample: 
#       concrete_action (str), 
#       description (str)
@app.post("/concrete_examples")
async def generate_actions(concreteExample: ConcreteExample):
    concreteExamples = generate_concrete_action_examples(f"Concrete Action: {concreteExample.concrete_action}, Description: {concreteExample.description}.")
    return{"concreteExamples": concreteExamples}