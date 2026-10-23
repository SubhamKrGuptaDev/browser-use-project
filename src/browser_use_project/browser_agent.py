import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent, Browser
from browser_use import ChatGoogle  # Use native browser-use google wrapper instead of langchain

load_dotenv()

async def main():
    # 1. Connect to your system Chrome browser
    browser = Browser.from_system_chrome()

    # 2. Initialize native Google LLM supported by browser-use
    # Make sure GEMINI_API_KEY or GOOGLE_API_KEY is in your .env file
    llm = ChatGoogle(model="gemini-2.5-flash")

    # 3. Define your task prompt
    task_prompt = "Go to github.com and check my notifications."

    # 4. Initialize and run the agent
    agent = Agent(
        task=task_prompt,
        llm=llm,
        browser=browser,
    )

    history = await agent.run()
    print(history.final_result())

if __name__ == "__main__":
    asyncio.run(main())