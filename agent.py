from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser
import asyncio
from dotenv import dotenv_values
config = dotenv_values(".env")
browser = Browser()
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash-preview-04-17")

USERNAME = config.get("USERNAME")
PASSWORD = config.get("PASSWORD")

GITHUB_URL = config.get("GITHUB_URL")

task_github=f"""
  Open browser, then go to {GITHUB_URL} and let me how many followers does he have
"""

task_linkedin=f"""
  Open browser, wait for user to select user profile if needed.
  Go to https://linkedin.com, login with username {USERNAME} and password {PASSWORD}. 
  Handle multi-factor authentication if prompted (user intervention may be required).
  Wait for user to login.
  Once logged in, navigate to the main messaging page.
  Carefully examine each unread message thread one by one.
  If a message thread appears to be ONLY a simple birthday wish (like 'Happy birthday!', 'HBD!', 'Hope you have a great day!'), respond with a short, polite thank you message. Choose randomly from variants like: 'Thanks so much!', 'Appreciate the birthday wishes!', 'Thank you!', 'Thanks for thinking of me!'.
  If a message thread contains MORE than just a simple birthday wish, OR is clearly not a birthday wish, DO NOT RESPOND. Just mark it as read (if possible by clicking into it) and move to the next.
  Prioritize accuracy: It's better to miss replying to a birthday wish than to reply incorrectly to a non-birthday message.
  Stop after checking/replying to about 10-15 unread messages or if there are no more unread messages.
  Provide a summary of actions taken (e.g., 'Replied to 5 birthday messages, marked 3 other messages as read')

"""

async def run_github_task():
  print("--- Running GitHub Follower Check ---")
  agent = Agent(
    task=task_github, # Feeding the GitHub task
    llm=llm,
    browser=browser
  )
  result = await agent.run()
  print(f"GitHub Result: {result}")
  await browser.close() # Close the browser when done

async def run_linkedin_task():
  print("--- Running LinkedIn Message Check ---")
  agent = Agent(
    task=task_linkedin,
    llm=llm,  
    browser=browser
  )
  result = await agent.run()
  print(f"LinkedIn Result: {result}")
  await browser.close() # Close the browser when done 

asyncio.run(run_github_task())