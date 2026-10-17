# Exercise 2 - Team Contract

**Course:** CS250 - Computational Thinking  
**Class:** 25A01  
**Team Name:** CS250 - Group 5  
**Project Title:** cs252-final-project  
**Individual Submission by:** Nguyen Duc Huy (Student ID: 25125014)  

---

## 1. Team Information

- **Course:** CS250 - Computational Thinking
- **Team Size:** 7 members
- **Team Name:** CS250 - Group 5
- **Project Title:** cs252-final-project
- **Group Repository:** [https://github.com/callmelucian/cs252-final-project](https://github.com/callmelucian/cs252-final-project)
- **Primary Communication Channel:** Messenger Group Chat & Google Sheets for Task Tracking
- **Instructor Contact Liaison:** Nguyen Tan Minh (Team Leader)

### Member Contact & Information Roster

| No. | Student ID | Full Name | Email | GitHub Username | Preferred Contact | Project Role |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 25125027 | Nguyen Tan Minh | ntminh2526@apcs.fitus.edu.vn | [callmelucian](https://github.com/callmelucian) | Messenger / Email | Team Leader |
| 2 | 25125084 | Tran Gia Huy | tghuy2533@apcs.fitus.edu.vn | [FubuGold](https://github.com/FubuGold) | Messenger | Main System Design |
| 3 | 25125050 | Bui Do Thien An | bdtan2516@apcs.fitus.edu.vn | [Gasmask-Chan](https://github.com/Gasmask-Chan) | Messenger | Algorithm & Logic Dev |
| 4 | **25125014** | **Nguyen Duc Huy** | ndhuy2526@apcs.fitus.edu.vn | [SpheraXX](https://github.com/SpheraXX) | Messenger / Email | Front-end Developer |
| 5 | 25125048 | Ly Tran Thai | ltthai2532@apcs.fitus.edu.vn | [LyTranThai](https://github.com/LyTranThai) | Messenger | Developer |
| 6 | 25125056 | Tran Dang Khoa | tdkhoa2529@apcs.fitus.edu.vn | [trankhoa8581](https://github.com/trankhoa8581) | Messenger | Backend Developer |
| 7 | 23125054 | Ngo Tan Dat | ntdat232@apcs.fitus.edu.vn | [diamondzone1](https://github.com/diamondzone1) | Messenger | Security & Data |

---

## 2. Team Goals and Expectations

- **Academic Goal:** Strive for excellence in all lab assignments and the course project, targeting an overall project grade of $\ge 9.0/10$.
- **Competency & Engineering Standard:**
  - Master and apply Computational Thinking paradigms and clean modern C++ Object-Oriented Programming (OOP).
  - Deliver a production-grade, maintainable codebase that serves as a standout portfolio piece on each member's GitHub profile.
- **Effort Commitment:**
  - Each member commits to investing at least **8 to 10 hours per week** in project-related activities (team meetings, design discussions, coding, code reviews, and documentation).
  - Commitment increases to **12 to 15 hours per week** during milestone sprints, milestone code freezes, and final presentation preparation.

---

## 3. Roles and Responsibilities

1. **Nguyen Tan Minh (Team Leader):** Roadmapping, sprint planning, task assignment, repository management, cross-module synchronization, and communication liaison with course staff.
2. **Tran Gia Huy (Main System Design):** High-level software architecture, UML class diagrams, interface abstractions, and enforcing Google C++ Style Guide standards.
3. **Bui Do Thien An (Algorithm & Logic Developer):** Research, design, and implementation of core computational algorithms, performance optimization, and complexity reduction.
4. **Nguyen Duc Huy (Front-end Developer):** Designing intuitive CLI/GUI user interfaces, input validation, user experience workflows, integration with backend handlers, and user documentation.
5. **Ly Tran Thai (Developer):** Feature implementation based on architectural specifications, writing robust utility routines and unit test suites.
6. **Tran Dang Khoa (Backend Developer):** Persistence layers, file I/O operations, resource lifecycle management (RAII), and core application services.
7. **Ngo Tan Dat (Security & Data):** Data structure security, input sanitization, integrity checking, and memory-safety audits.

**Role Rotation Policy:**
- If a member completes their assigned sprint backlog early or a specific module experiences a technical bottleneck, the Team Leader may reallocate tasks to enable cross-functional support upon mutual agreement.
- Members wishing to rotate responsibilities (e.g., transition from Dev to System Architecture or Testing) can propose the adjustment during weekly sprint reviews.

---

## 4. Communication

- **Primary Channels:** Messenger group for daily communications, quick queries, and emergency notices; Google Sheets for transparent task status tracking.
- **Expected Response Times:**
  - *Standard messages:* Within **24 hours**.
  - *Urgent notices (tagged `@all` or time-critical blocking issues):* Within **4 to 6 hours**.
  - *Acknowledgment rule:* Members must react (with an emoji) to acknowledge receipt of critical announcements. If instructions are unclear, the member must ask for clarification directly in the chat.
- **Instructor Contact Point:** To prevent conflicting or duplicate inquiries, only the Team Leader (Nguyen Tan Minh) is authorized to communicate officially with the lecturer and TAs on behalf of the group.

---

## 5. Meetings

- **Cadence:** At least **once per week**, scheduled prior to the weekly CS250 lab session, with supplementary ad-hoc sessions if urgent architectural decisions arise.
- **Format & Venue:**
  - *In-person:* Campus study rooms or HCMUS library facilities before/after scheduled class hours.
  - *Online:* Google Meet or Discord group voice channels for evening or weekend syncs.
- **Meeting Etiquette & Rules:**
  - *Agendas:* The Team Leader distributes the meeting agenda at least **12 hours in advance**.
  - *Meeting Minutes:* A designated secretary (rotating weekly) documents all decisions, action items, and deadlines into `docs/meeting_notes.md` within 24 hours post-meeting.
  - *Punctuality & Absences:* Punctual attendance is mandatory. In cases of emergency, members must notify the Team Leader at least **6 hours in advance** and submit an async status update.

---

## 6. Work Process and Standards

- **Task Management:** Managed transparently via Google Sheets and GitHub Projects/Issues. Each task must have a single primary owner (Assignee), a clear Definition of Done (DoD), and an explicit deadline.
- **Internal Deadlines:** All code, assets, and documentation must be submitted for peer review **at least 48 hours before official university submission deadlines**, providing ample buffer for integration testing and bug fixes.
- **Git Workflow & Hygiene:** Strictly adhering to the protocol established in `AGENT.md`:
  - Direct commits to the `main` branch are strictly prohibited.
  - Feature branches follow standard naming: `feature/<module-name>`, `fix/<issue-name>`, or `<initials>/<feature-name>`.
  - Atomic conventional commits: `feat(...)`, `fix(...)`, `refactor(...)`, `docs(...)`.
  - Mandatory Pull Request (PR) review: Every PR must be approved by at least **one peer reviewer or the Team Leader** before merging.
- **Code & Documentation Quality:**
  - Code must adhere to the Google C++ Style Guide (`PascalCase` for types, `camelCase` for functions/variables, `m_PascalCase` for class members, `CONSTANT_CASE` for constants).
  - All lab and milestone reports must be authored in GitHub-Flavored Markdown and rendered cleanly into standalone `.html` or `.pdf` formats.

---

## 7. Decision Making

- Open technical and procedural discussions are actively encouraged within the team.
- **Consensus & Majority Vote:** Technical approaches are decided by consensus whenever possible. When divergent opinions persist, decisions are resolved by a **majority vote (> 50% of active members)**.
- **Final Say (Deadlock Resolution):** In the event of an exact tie (e.g., 3-3 during an absence) or protracted indecision, the **Team Leader has the final tie-breaking vote** in the best interest of project timeline and deliverables.

---

## 8. Conflict Resolution

Disagreements are resolved through a structured 3-tier escalation framework:
1. **Tier 1 - Direct Peer Dialogue:** The parties involved discuss the issue directly, professionally, and objectively, focusing strictly on technical data and project objectives.
2. **Tier 2 - Team Mediation:** If unresolved after 24 hours, the issue is escalated to the full team during an extraordinary sync. Both perspectives are presented, followed by open debate and a binding majority vote.
3. **Tier 3 - Course Staff Consultation:** If the impasse persists and jeopardizes project delivery, the Team Leader formally requests guidance from the course instructor or teaching assistants for authoritative arbitration.

---

## 9. Accountability and Consequences

### 9.1. Defined Violations
- Missing internal deadlines without prior notice or valid justification.
- Unexcused absence from two consecutive team meetings.
- Failing to respond to team communications past stipulated timeframes (> 48 hours for normal messages, > 12 hours for urgent notices).
- Submitting sub-standard, broken, or unformatted code that fails build checks.
- Plagiarism, unauthorized code duplication, or undisclosed AI generation.

### 9.2. Escalation & Disciplinary Ladder
- **First Offense (Informal Warning):** Direct reminder from the Team Leader; the member must address the delinquent deliverable within 24 hours.
- **Second Offense (Formal Warning):** Warning documented in meeting minutes; partial redistribution of critical task dependencies to ensure progress continuity.
- **Third Offense (Course Staff Escalation):** The team files an official report to the course instructor for guidance on contribution assessment.

### 9.3. Contribution Evaluation
- Contribution is quantified through Git commit metrics, validated PR merges, peer review participation, meeting attendance, and adherence to internal deadlines. Final contribution ratios will be accurately declared in milestone reports.

---

## 10. Academic Integrity and AI Use

- **Originality & Anti-Plagiarism:** Every line of code, documentation, and analysis must reflect the team's genuine understanding. Direct copying from external sources or other student teams without clear attribution is strictly prohibited.
- **Generative AI Guidelines:**
  - GenAI tools (ChatGPT, Claude, Gemini, GitHub Copilot) may be utilized solely for ideation, syntax lookups, architectural skeleton generation, debugging assistance, and phrasing polish.
  - No member may commit code generated by AI without thoroughly reading, understanding, refactoring, and verifying every line.
- **AI Logging Protocol:**
  - All substantial AI interactions must be documented in `AI log/week_XX.md` adhering strictly to the citation format established in `AGENT.md`:
    > `– <Tool>. <Model/Version>, <Provider>, <Interface/URL>, accessed <HH:MM> on <Month DD, YYYY>, prompt: “<Prompt>”, used to <Purpose>; <AI contribution>, <Student verification and testing details>.`

---

## 11. Changing the Contract

- **Proposal:** Any member may propose amendments or revisions to this contract during any scheduled team meeting.
- **Ratification Threshold:** Amendments require ratification by a **supermajority of at least 70% (at least 5 out of 7 members)**.
- **Version Control:** Approved modifications will be updated directly in this contract file and committed to the repository to maintain team alignment.

---

## 12. Signatures and Member Agreement

By signing below, all 7 members confirm that they have reviewed, understood, and agreed to abide by all principles and rules set forth in this Team Contract:

| No. | Member Full Name | Student ID | Date | Agreement Status |
| :---: | :--- | :---: | :---: | :---: |
| 1 | Nguyen Tan Minh | 25125027 | Oct 17, 2026 | **Agreed & Signed** |
| 2 | Tran Gia Huy | 25125084 | Oct 17, 2026 | **Agreed & Signed** |
| 3 | Bui Do Thien An | 25125050 | Oct 17, 2026 | **Agreed & Signed** |
| 4 | **Nguyen Duc Huy** | **25125014** | **Oct 17, 2026** | **Agreed & Signed** |
| 5 | Ly Tran Thai | 25125048 | Oct 17, 2026 | **Agreed & Signed** |
| 6 | Tran Dang Khoa | 25125056 | Oct 17, 2026 | **Agreed & Signed** |
| 7 | Ngo Tan Dat | 23125054 | Oct 17, 2026 | **Agreed & Signed** |
