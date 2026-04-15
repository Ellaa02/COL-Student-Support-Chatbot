import google.generativeai as genai
import pandas as pd

#  Configuration
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-2.0-flash")

SYSTEM_PROMPT = """
You are the COL Student Support Assistant for William & Mary's
Center for Online Learning. Answer student questions warmly and 
concisely using ONLY the knowledge base context provided below.
If you don't know, say: "I don't have that information. Please 
contact online@mason.wm.edu"
"""

#  Knowledge Base (simplified) 
KNOWLEDGE_BASE = {
    "add drop deadline": (
        "The add/drop period ends at 11:59 PM on Sunday of the "
        "first week of the session for most online classes. "
        "Reference: wm.edu/offices/registrar/"
    ),
    "canvas access": (
        "Canvas opens approximately one week before your term "
        "starts. If you cannot see your course after term begins, "
        "contact online@mason.wm.edu"
    ),
    "password reset": (
        "Reset your W&M password at changepassword.wm.edu. "
        "For locked accounts, contact IT: wm.edu/offices/it/gethelp/"
    ),
    "beta gamma sigma": (
        "Beta Gamma Sigma is an international business honor "
        "society. Membership is invitation-only for students "
        "ranked in the top 20% of their program."
    ),
    "graduation": None,  # escalate — never answer directly
    "withdraw": (
        "Withdrawal deadline is 31 days after class starts. "
        "A 'W' appears on your transcript and tuition is charged. "
        "Reference: catalog.wm.edu"
    ),
}

###          Agentic Routing      ###   
ESCALATE   = ["graduation", "how many courses", "course load"]
CRISIS     = ["stressed", "overwhelmed", "crisis", "not okay"]
GREETINGS  = ["hi", "hello", "hey", "start"]

def route(question: str) -> str:
    q = question.lower()

    # 1. Greeting
    if any(w in q for w in GREETINGS) and len(q.split()) <= 3:
        return "GREET"

    # 2. Crisis — intercepts BEFORE AI generation
    if any(w in q for w in CRISIS):
        return "CRISIS"

    # 3. Hard escalation
    if any(w in q for w in ESCALATE):
        return "ESCALATE"

    # 4. Search knowledge base
    for keyword, answer in KNOWLEDGE_BASE.items():
        if keyword in q:
            return "ESCALATE" if answer is None else f"KB:{answer}"

    return "UNKNOWN"

#  Response Generator 
def respond(question: str) -> str:
    action = route(question)

    if action == "GREET":
        return (
            "Hi! I'm the W&M COL Student Support Assistant.\n"
            "I can help with: registration, Canvas, passwords,\n"
            "academic policies, Beta Gamma Sigma, and more.\n"
            "What can I help you with today?"
        )

    if action == "CRISIS":
        return (
            "I'm sorry to hear you're struggling.\n"
            "Please reach out for support:\n"
            "  W&M Counseling: wm.edu/offices/counselingcenter/\n"
            "  Crisis Line: call or text 988 (24/7)"
        )

    if action == "ESCALATE":
        return (
            "That question depends on your individual situation.\n"
            "Please contact the Student Support Center:\n"
            "  Email: online@mason.wm.edu\n"
            "  Hours: Mon-Fri, business hours"
        )

    if action.startswith("KB:"):
        context = action[3:]
        prompt  = f"{SYSTEM_PROMPT}\n\nKB: {context}\n\nQ: {question}"
        return model.generate_content(prompt).text

    return (
        "I don't have that information.\n"
        "Please contact: online@mason.wm.edu"
    )

#  Chat Loop 
print("COL Student Support Assistant  |  type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("quit", "exit", "bye"):
        print("Bot: Take care! Good luck with your studies.")
        break
    if user_input:
        print(f"Bot: {respond(user_input)}\n")
