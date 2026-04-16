# 🎓 AI Student Support Chatbot
### Center for Online Learning — William & Mary, Mason School of Business

> **An agentic AI chatbot that answers student questions about online graduate programs, routes complex inquiries to human advisors, and updates itself when the knowledge base changes — no code required.**

---

![W&M COL Banner](https://img.shields.io/badge/William%20%26%20Mary-Center%20for%20Online%20Learning-115740?style=for-the-badge)
![Built With](https://img.shields.io/badge/Built%20With-Microsoft%20Copilot%20Studio-0078D4?style=for-the-badge&logo=microsoft)
![Status](https://img.shields.io/badge/Status-Prototype%20Complete-4ADE80?style=for-the-badge)

---
<img width="799" height="521" alt="image" src="https://github.com/user-attachments/assets/793cc7ad-c34f-4422-b504-05eea3fb98ba" />

## 📌 Why This Matters

Online graduate students at W&M face a common frustration: getting quick, reliable answers to routine questions — about registration deadlines, Canvas access, passwords, graduation requirements — currently requires emailing the Student Support Center and waiting for a response.

For a program serving working professionals across time zones, **response lag is a real barrier to student success.**

This project directly addresses that gap. By deploying an AI-powered chatbot grounded in W&M's own knowledge base, the Center for Online Learning can:

- **Deflect 60–70% of routine support inquiries** to self-service
- **Provide 24/7 availability** without additional staffing
- **Maintain accuracy** through a no-code update workflow anyone can manage
- **Preserve human judgment** for complex, individual-specific situations through intelligent escalation

---

## 👥 Author List

| Name | GitHub |
|------|--------|
| [Ella Pan] | [@Ellaa02](https://github.com/Ellaa02) |
| [Rachel Cole] | [@rmcole2488](https://github.com/rmcole2488) |
| [Andrew Piercy] | [@ampiercy](https://github.com/ampiercy) |
| [Walker Marsh] | [@walkermarsh7](https://github.com/walkermarsh7) |

---

## 🔭 Project Scope

**Client:** Center for Online Learning (COL), Raymond A. Mason School of Business, William & Mary

**Problem:** Online graduate students frequently contact the Student Support Center with routine, repetitive questions that could be answered automatically, creating bottlenecks for both students and staff.

**Solution scope:**
- A chatbot covering **70+ FAQ entries** sourced directly from COL staff
- Deployed within W&M's existing **Microsoft Copilot Studio** environment (no new licensing required)
- Knowledge base managed via a **single Excel file in SharePoint** — editable by non-technical staff
- Agentic design with **autonomous routing**: the bot decides when to answer vs. when to escalate to a human advisor
- **Out of scope:** Integration with live W&M systems (Banner, Degree Works, Canvas APIs), personalized student record access, and financial aid queries

---

## 📋 Project Details

### The Business Problem

The COL Student Support Center receives a high volume of repetitive student inquiries — questions about add/drop deadlines, Canvas access, password resets, and program information. These are time-consuming for staff but individually simple to answer. The opportunity: automate the routine, preserve human attention for what actually requires it.

### Agentic Design Architecture

This project implements an **agentic AI** design with three core autonomous behaviors:

```
Student Question
      ↓
[Agent Decision Layer]
      ↓
┌─────────────────────────────────────────┐
│  Can I answer from the knowledge base?  │
├──────────────┬──────────────────────────┤
│     YES      │           NO             │
│      ↓       │            ↓             │
│  Generate    │  Is it sensitive/        │
│  answer +    │  individual-specific?    │
│  link        │       ↓                  │
│              │  Route to human:         │
│              │  online@mason.wm.edu     │
└──────────────┴──────────────────────────┘
```

**Agentic elements present in this design:**

| Agentic Capability | How It's Implemented |
|---|---|
| **Autonomous decision-making** | Bot decides independently whether to answer, escalate, or request clarification |
| **Tool use / knowledge retrieval** | Bot searches the SharePoint knowledge base on every query using RAG (Retrieval-Augmented Generation) |
| **Goal-directed behavior** | Bot maintains the goal of student resolution across multi-turn conversations |
| **Dynamic topic routing** | Custom topics intercept specific intents (greeting, escalation, crisis) before AI generation |
| **Self-updating knowledge** | Knowledge base syncs automatically when the Excel file is updated — no redeployment needed |

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    STUDENT INTERFACE                         │
│         Embedded chat widget on online.mason.wm.edu         │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│               MICROSOFT COPILOT STUDIO                       │
│                                                              │
│  ┌─────────────────┐     ┌──────────────────────────────┐   │
│  │  System Prompt  │     │     Topic Router              │   │
│  │  (GitHub Higher │     │  Greeting / Start Over /      │   │
│  │  Ed Template)   │     │  Escalate / Emergency / etc.  │   │
│  └────────┬────────┘     └──────────────┬───────────────┘   │
│           │                             │                    │
│  ┌────────▼─────────────────────────────▼───────────────┐   │
│  │              AI Response Engine                       │   │
│  │         (Claude Sonnet / Microsoft AI)                │   │
│  └────────────────────────┬──────────────────────────────┘  │
│                           │                                  │
│  ┌────────────────────────▼──────────────────────────────┐  │
│  │              Knowledge Base (RAG)                      │  │
│  │   KB_Tracker_WithAnswers.xlsx + Amanda's PDFs          │  │
│  │   Hosted in SharePoint: BUS-OnlineGraduatePrograms     │  │
│  └────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                          │
                          │ Escalation
                          ▼
              online@mason.wm.edu (Human Advisor)
```

### Knowledge Base

The knowledge base covers 9 categories with 74 question-answer pairs:

| Category | Questions | Escalation Required |
|---|---|---|
| Program Curriculum | 15 | Sometimes (OMBA 2.0 individual plans) |
| Registration | 10 | Yes (course load, cross-program) |
| Academic Policies | 9 | No |
| Canvas Course Access | 10 | No |
| Password Resets | 6 | No |
| General Campus Information | 7 | No |
| Graduation Requirements | 1 | Yes (all graduation queries) |
| Beta Gamma Sigma | 10 | Sometimes (eligibility disputes) |
| Technical Support | 6 | No |

### Prompt Engineering Approach

The bot's identity, tone, and behavioral rules were built using the **Higher Education Agent template** from Amanda Goldstein's prompt template library ([cf-gbroady/PromptTemplateLibrary](https://github.com/cf-gbroady/PromptTemplateLibrary)), adapted specifically for W&M COL's context.

Key prompt design decisions:
- **Role-constrained responses:** Bot only answers from the knowledge base, never fabricates policies
- **Escalation rules embedded in prompt:** Specific question types trigger human routing regardless of knowledge base content
- **Tone calibration:** Warm, professional, and concise — consistent with W&M's academic environment
- **Dynamic date awareness:** Uses `{{today}}` to ensure time-sensitive answers (registration deadlines) are contextually accurate

### Conversation Topics (Agentic Routing Layer)

| Topic | Trigger Intent | Bot Behavior |
|---|---|---|
| Conversation Start | Chat opens | Warm greeting + capability overview |
| Greeting | "hi", "hello", "hey" | Re-introduces capabilities |
| Escalate to Human | "talk to someone", "contact support" | Surfaces email + hours immediately |
| Start Over | "reset", "nevermind", "start over" | Clears conversation, returns to greeting |
| New Student | "just enrolled", "new student" | Curated first-steps checklist |
| Emergency / Distress | "stressed", "crisis", "overwhelmed" | W&M counseling + 988 crisis line |
| Off Topic | Unrelated queries | Politely redirects to supported topics |
| Thank You / Goodbye | "thanks", "bye" | Warm closing + reminds of support email |
| Feedback | "wrong answer", "that's incorrect" | Acknowledges + routes to human |

### Live Chatbot Demo

Try our deployed chatbot prototype here (Note: This may require you to login to Microsoft using W&M Credentials):

👉 [Launch Student Support Chatbot](https://copilotstudio.microsoft.com/environments/Default-b93cbc3e-661d-4058-8693-a897b924b8d7/bots/50bf6e5c-3a2c-f111-88b4-7ced8d6f06c2/publish)

---

## 🔮 What's Next?

### Near-Term (Next Semester)

- **Full SharePoint integration** once admin-level publishing permissions are resolved with W&M IT
- **Live embed on online.mason.wm.edu** via the Copilot Studio embed snippet
- **Knowledge base completion review** with Amanda — a few answers still need verification against internal W&M documents (OMBA 2.0 specialization details, BGS GPA thresholds)

### Medium-Term

- **Analytics dashboard review** — Copilot Studio provides built-in analytics showing which questions are asked most, which escalate most, and where the bot fails. Monthly review cycle recommended.
- **Structured expansion** — as new programs launch or policies change, the Excel-based update workflow means no developer involvement is ever needed
- **Teams channel integration** — Copilot Studio supports native Microsoft Teams handoff, enabling real-time agent escalation during business hours

### Long-Term

- **Banner/Degree Works integration** — if W&M IT enables API access, the bot could answer personalized questions like "what courses do I still need?" rather than routing everything individual to human advisors
- **Multilingual support** — Copilot Studio supports multiple languages; relevant as international enrollment grows
- **Proactive notifications** — future versions could push reminders about upcoming deadlines rather than waiting for students to ask

---

## ⚖️ Responsible AI Considerations

### What we built in

| Risk | Mitigation |
|---|---|
| **Hallucination / fabricated policies** | Bot is grounded strictly in the knowledge base using RAG; fallback message routes unknowns to humans |
| **Over-reliance on AI for sensitive decisions** | Hard escalation rules built into prompt for graduation, course load, and individual academic planning |
| **Student distress mishandled** | Emergency topic intercepts distress language before AI generation and surfaces W&M Counseling + 988 |
| **FERPA / data privacy** | Bot has zero access to student records; cannot request, store, or transmit personal information |
| **Outdated information causing harm** | Excel-based update workflow with semester review schedule; annual URL verification checklist |

### Ongoing concerns

- **Accountability gap:** If the bot gives incorrect information and a student acts on it, responsibility is currently unclear. A clear disclaimer and easy escalation path partially addresses this but does not fully resolve it.
- **Equity of access:** Students with lower digital literacy or accessibility needs may interact differently with a chatbot interface. The bot should be tested with screen readers and accessibility tools before full deployment.
- **Dependency risk:** If the COL team relies on the bot without maintaining the knowledge base, answer quality will degrade over time. The maintenance schedule in the handoff documentation addresses this directly.
- **Content currency:** Registration deadlines, program requirements, and policy details change every semester. No automated mechanism currently detects stale content — this depends on human review.

---

## 📚 References

### Research Paper

> **[Primary Paper — Replace with your selected paper]**
> 
> Suggested: Kang, M., & Lee, H. (2023). Conversational AI in higher education: A systematic review of chatbot applications for student support services. *Computers & Education*, 198, 104756. https://doi.org/10.1016/j.compedu.2023.104756

### Tools & Platforms

- Microsoft Copilot Studio — https://copilotstudio.microsoft.com
- Microsoft SharePoint — https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration
- W&M Center for Online Learning — https://online.mason.wm.edu/

### Prompt Engineering Resources

- Goldstein, A. (2025). *PromptTemplateLibrary* [GitHub repository]. https://github.com/cf-gbroady/PromptTemplateLibrary
- Microsoft. (2025). *Microsoft Copilot Studio documentation*. https://learn.microsoft.com/en-us/microsoft-copilot-studio/

### Agentic AI Frameworks

- Wang, L., et al. (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science*, 18(6). https://doi.org/10.1007/s11704-024-40231-1
- Microsoft. (2025). *Build generative AI-powered bots with Copilot Studio*. https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-generative-answers

---

*This project was developed as a course deliverable. The client's full identity is not disclosed without explicit permission.*
