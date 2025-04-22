from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser
import asyncio
import os
from dotenv import dotenv_values
config = dotenv_values(".env")
browser = Browser()
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash-preview-04-17")

USERNAME = config.get("USERNAME")
PASSWORD = config.get("PASSWORD")

GITHUB_URL = config.get("GITHUB_URL")

async def main():
  agent = Agent(
    task=f"""
      Go to https://linkedin.com, login with username: '{USERNAME}' and password: '{PASSWORD}'. 
      Then go to messages, and mark all messages as read, on by one, by responding something like the following:
      'Thanks, I appreciate it',  'Thank you for the wishes', etc.
      Do not respond to any other message which is not a birthday wish. Just mark it as read.
    """,
    # task=f"""
    #   Open browser, {GITHUB_URL} then go to  and let me how many followers does he have
    # """,
    llm=llm,
    browser=browser
  )
  result = await agent.run()
  print(result)

asyncio.run(main())