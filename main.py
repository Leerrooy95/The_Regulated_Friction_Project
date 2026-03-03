import asyncio
import json
import subprocess
import os
from copilot import CopilotClient, PermissionHandler
from gradient_adk import entrypoint


@entrypoint
async def main(input_data: dict):
    print("🚀 OSINT Immune System Awakening...")

    # 1. Trigger the Spiders (The Heavy Machinery)
    # This runs your scrapers and saves the data to your 'data' folder
    print("🕷️ Triggering Spiders: Federal Register & DOJ...")
    try:
        subprocess.run(["scrapy", "crawl", "federal_register_eo",
                       "-O", "data/reg_data.json"], check=True)
        subprocess.run(["scrapy", "crawl", "doj_press_releases",
                       "-O", "data/friction_data.json"], check=True)
    except Exception as e:
        print(f"❌ Error running spiders: {e}")
        return {"status": "error", "message": str(e)}

    # 2. Load the Scraped Data & Your Rules
    print("📂 Loading data for analysis...")
    with open("data/reg_data.json", "r") as f:
        reg_data = json.load(f)
    with open("data/friction_data.json", "r") as f:
        friction_data = json.load(f)
    with open(".github/copilot-instructions.md", "r") as f:
        osint_rules = f.read()

    # 3. Wake up the Brain (Claude Opus 4.6)
    client = CopilotClient()
    await client.start()

    session = await client.create_session({
        "model": "claude-opus-4.6",
        "instructions": osint_rules,  # Your OSINT methodology
        "reasoning_effort": "high",
        "on_permission_request": PermissionHandler.approve_all
    })

    # 4. Perform the "Regulated Friction" Analysis
    print("🧠 Correlating Data Streams (this takes about 60-90 seconds)...")

    # We only send the top 100 recent items to keep things focused
    prompt = (
        f"Analyze these two data streams for 'Regulated Friction':\n\n"
        f"COMPLIANCE DATA (Federal Register): {json.dumps(reg_data[:100])}\n\n"
        f"FRICTION DATA (DOJ Press): {json.dumps(friction_data[:100])}\n\n"
        "Identify any correlations within a 7-day window. Output a HIGH ALERT or STABLE report."
    )

    # We set timeout to 300 (5 minutes) so the AI has plenty of time to 'think'
    response = await session.send_and_wait({"prompt": prompt}, timeout=300)

    # 5. Output the Results
    print("-" * 30)
    print(f"OSINT SIGNAL REPORT:\n{response.data.content}")
    print("-" * 30)

    # Close the connection
    await client.stop()
    return {"status": "success", "report": response.data.content}

if __name__ == "__main__":
    # This runs the script locally when you type 'python3 main.py'
    asyncio.run(main({}))
