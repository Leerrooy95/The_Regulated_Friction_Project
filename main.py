import json
import os
from copilot import CopilotClient, PermissionHandler
from gradient_adk import entrypoint, RequestContext

@entrypoint
async def main(_input_data: dict, _context: RequestContext):
    print("🚀 OSINT Immune System Awakening...")

    # 1. Load the Scraped Data (Provided by your 8 AM GitHub Action)
    print("📂 Loading data for analysis...")
    try:
        with open("data/reg_data.json", "r") as f:
            reg_data = json.load(f)
        with open("data/friction_data.json", "r") as f:
            friction_data = json.load(f)
    except FileNotFoundError:
        print("❌ Data not found. Waiting for GitHub Action to run Scrapy.")
        return {"status": "error", "message": "Missing output data"}
        
    # Fallback if .github folder is not deployed
    osint_rules = "You are an OSINT analyst looking for Regulated Friction."
    rules_path = ".github/copilot-instructions.md"
    if os.path.exists(rules_path):
        with open(rules_path, "r") as f:
            osint_rules = f.read()

    # 2. Wake up the Brain (Claude Opus 4.6)
    client = CopilotClient()
    await client.start()

    session = await client.create_session({
        "model": "claude-opus-4.6",
        "instructions": osint_rules,
        "reasoning_effort": "high",
        "on_permission_request": PermissionHandler.approve_all
    })

    # 3. Perform the "Regulated Friction" Analysis
    print("🧠 Correlating Data Streams (this takes about 60-90 seconds)...")
    prompt = (
        f"Analyze these two data streams for 'Regulated Friction':\n\n"
        f"COMPLIANCE DATA (Federal Register): {json.dumps(reg_data[:100])}\n\n"
        f"FRICTION DATA (DOJ Press): {json.dumps(friction_data[:100])}\n\n"
        "Identify any correlations within a 7-day window. Output a HIGH ALERT or STABLE report."
    )

    response = await session.send_and_wait({"prompt": prompt}, timeout=300)

    # 4. Save and Output the Results
    print("-" * 30)
    print("💾 Saving OSINT Signal Report to output/findings.json...")
    
    os.makedirs("output", exist_ok=True)
    with open("output/findings.json", "w") as f:
        # Saving the AI's actual text response so the dashboard can read it
        json.dump({"signal_report": response.data.content}, f, indent=2)

    print("✅ Analysis Complete.")
    return {"status": "success", "report": response.data.content}