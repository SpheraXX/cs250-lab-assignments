# Exercise 5 - Responsible AI Usage

**Course:** CS250 - Computational Thinking  
**Class:** 25A01  
**Student Name:** Nguyen Duc Huy  
**Student ID:** 25125014  
**GitHub Username:** SpheraXX  

---

## Introduction

Artificial Intelligence (AI), particularly Large Language Models (LLMs) and intelligent code generation assistants, has transformed modern software development and academic research. In technical disciplines like Computer Science, these tools offer immense productivity leverage. However, uncritical reliance on AI introduces severe risks, including cognitive atrophy, academic dishonesty, intellectual property infringement, security vulnerabilities, and logic flaws caused by model hallucinations.

This report documents my hands-on experience utilizing AI since 2024 and outlines a **6-Stage Closed-Loop Human-in-the-Loop Workflow** developed to ensure rigorous, safe, and responsible AI integration, aligned with university integrity standards and the principles outlined in the VNPT AI Responsible AI framework.

---

## 1. Have you used AI before?

I have actively and systematically integrated generative AI tools into my academic and software engineering workflows since **early 2024**.

### Frequently Utilized Tooling:
- **Conversational & Reasoning Models:** ChatGPT (GPT-4 / GPT-4o), Claude 3.5 Sonnet, Google Gemini.
- **In-Editor Code Assistants:** GitHub Copilot, Cursor AI / Antigravity IDE.
- **Research & Search Engines:** Perplexity AI, Google Scholar AI integrations.

### Practical Engineering & Academic Contexts:
1. **Architectural Exploration & Ideation:** Evaluating design trade-offs between architectural patterns (e.g., comparing modular OOP class decompositions vs. procedural logic) before committing to implementation.
2. **Syntax Lookup & Standard Library Deep Dives:** Navigating modern C++ language standards (C++17/20), exploring memory management constructs (`std::unique_ptr`, `std::shared_ptr`, custom deleters), and understanding template metaprogramming conventions.
3. **Compiler Error Diagnostics & Refactoring:** Deciphering dense compiler template instantiation errors and identifying memory leaks or segmentation faults.
4. **Documentation Scaffolding:** Generating standardized API documentation skeletons, drafting markdown tables, and formatting structured reports.

> **Guiding Principle:** AI serves strictly as an **"Intellectual Copilot"** that accelerates boilerplate tasks and enhances cognitive breadth. It must never supersede the engineer's foundational critical thinking, analytical reasoning, and personal accountability for the final deliverable.

---

## 2. Do you have any experience or tips for using AI?

Through extensive trial, error, and practical software development, I have formalized a disciplined **6-Stage Closed-Loop Human-in-the-Loop Workflow**. This iterative framework ensures that human oversight remains the authoritative control gate at every stage:

```
[1. Structured Planning] ➔ [2. Plan Review] ➔ [3. Scoped Execution] 
                                                        │
[6. Context Updating] 🠄 [5. Empirical Verification] 🠄 [4. Active Monitoring]
```

### The 6-Stage Responsible AI Workflow:

#### Stage 1: Structured Planning
- Never initiate an open-ended or ambiguous prompt. Before generating any code or analytical text, instruct the AI to collaboratively outline a detailed **Implementation Action Plan**.
- Explicitly supply the operational boundaries: problem domain, input/output schemas, technical constraints (language standard, disallowed libraries, performance budgets), and clear definitions of done.

#### Stage 2: Critical Plan Review
- Scrutinize the AI's proposed plan with a skeptical, adversarial mindset.
- Identify and eliminate ungrounded assumptions, unnecessary architectural bloat, or hallucinations (such as recommending non-standard external dependencies). Only when the plan satisfies project constraints is approval granted to proceed.

#### Stage 3: Scoped, Incremental Execution
- Deconstruct complex tasks into atomic, decoupled modules.
- Prompt the model to address one function, interface, or conceptual section at a time. **Avoid prompting for monolithic codebase generation**, as large unsegmented outputs obscure hidden bugs and make validation exponentially harder.

#### Stage 4: Active Monitoring & Real-Time Intervention
- Closely track the AI's streaming response and intermediate logic.
- The moment the model drifts off-topic, invents non-existent APIs, or violates coding conventions, **immediately abort generation**. Intervene and refine the prompt prompt-context rather than allowing the model to compound the error.

#### Stage 5: Independent Empirical Verification & Peer Review
- This constitutes the core ethical and technical boundary:
  - **100% Comprehension:** The student must be capable of explaining every line of generated code down to memory allocation mechanics.
  - **Empirical Testing:** Compile locally using strict warning flags (`-Wall -Wextra -Wpedantic`) and execute against robust unit tests, edge cases, and unexpected inputs.
  - **Textbook Alignment:** Cross-reference conceptual explanations against authoritative university textbooks and official language standards (e.g., ISO C++ reference manuals).

#### Stage 6: Refinement, Error Correction & Context Updating
- When bugs or inefficiencies are discovered, correct them directly and communicate precise diagnostic feedback to the model to explain why the previous output was flawed.
- **Update System Context & Memory:** Incorporate the discovered constraints or anti-patterns into persistent repository rules (such as `AGENT.md` or system prompt guidelines). This creates a compounding feedback loop that prevents identical mistakes from recurring in future engineering cycles.

---

## 3. Alignment with Responsible AI Core Principles

This workflow directly embodies the foundational pillars outlined in academic literature and the VNPT AI framework:

1. **Accountability:** The student retains 100% ultimate responsibility for the correctness, performance, and security of every submitted artifact. Blaming an AI model for an error is categorically unacceptable.
2. **Transparency & Rigorous Citation:** All AI interactions are documented openly via an AI Usage Declaration and dedicated weekly logs (`AI log/week_XX.md`), acknowledging prompts, model versions, and human intervention points.
3. **Data Privacy & Confidentiality:** No proprietary credentials, private authentication tokens, or confidential institutional data are ever transmitted to third-party AI endpoints.
4. **Academic Integrity & Fairness:** AI is harnessed to deepen conceptual mastery and hone Computational Thinking, not as an evasive shortcut to bypass essential cognitive labor.
