import asyncio
from droidrun import AdbTools, DroidAgent, DroidrunConfig
from llama_index.llms.google_genai import GoogleGenAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_user_input():
    print("\n=== Social Media Auto Poster ===\n")

    while True:
        caption = input("Enter post text:\n> ").strip()
        if caption:
            break
        print("❌ You didn't give anything to post. Please enter valid text to post.\n")

    hashtags = input("\nEnter hashtags (optional):\n> ").strip()

    supported_platforms = {"linkedin", "x"}

    while True:
        platforms = input(
            "\nAllowed platforms: LinkedIn, X\nSelect platforms (comma separated):\n> "
        ).strip()

        platform_list = [p.strip().lower() for p in platforms.split(",") if p.strip()]

        if not platform_list:
            print("❌ Please select at least one platform.\n")
            continue

        invalid = [p for p in platform_list if p not in supported_platforms]

        if invalid:
            print(
                f"❌ Unsupported platform(s): {', '.join(invalid)}\n"
                "For now, we only support cross-posting on LinkedIn and X.\n"
            )
            continue

        break

    return caption, hashtags, platform_list



async def post_to_platform(platform, post_text):
    tools = AdbTools()

    llm = GoogleGenAI( 
        model="models/gemini-2.0-flash"
    )

    goal = ""

    if platform == 'x':
        goal = f"""
    Open google chrome goto 'x.com'. close if any popup appears by denying them then
    Create a new post with the following content:
    "{post_text}"
    Publish the post.
    """
    else:
        goal = f"""
    Open {platform}.
    Create a new post with the following content:
    "{post_text}"
    Publish the post.
    """

    agent = DroidAgent(
        goal=goal.strip(),
        llms={
            "manager": llm,
            "executor": llm
        },
        tools=tools,
        config=DroidrunConfig()
    )

    result = await agent.run()
    print(f"✅ {platform.upper()}:", result.success)


async def main():
    caption, hashtags, platforms = get_user_input()
    post_text = f"{caption}\n\n{hashtags}"

    for platform in platforms:
        print(f"\n📱 Posting to {platform}...")
        await post_to_platform(platform, post_text)
        await asyncio.sleep(2)


if __name__ == "__main__":
    asyncio.run(main())
