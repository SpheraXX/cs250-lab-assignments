# Exercise 3 - Individual Proposal for the Course Project

**Course:** CS250 - Computational Thinking  
**Class:** 25A01  
**Student Name:** Nguyen Duc Huy  
**Student ID:** 25125014  
**GitHub Username:** SpheraXX  

---

# PROJECT PROPOSAL: Multimodal Retrieval & Automation-First LMS for Private Tutors and Small/Mid-sized Classes

**Project Identifier:** Multimodal Retrieval & Automation-First LMS  
**Domain:** Educational Technology (EdTech), Multimodal Artificial Intelligence, Workflow Automation Systems

---

## 1. Problem Statement & Real-World Context

Private tutors and instructors managing boutique classes (ranging from 5 to 30 students) face acute administrative friction that severely degrades pedagogical efficacy:

- **Heavy Administrative Overhead:** Tutors spend excessive hours manually managing homework submissions across fragmented channels (e.g., compressed photos sent via messaging apps), hand-grading free-response calculations step-by-step, calculating grade totals, maintaining spreadsheets, and drafting tailored progress reports for each individual parent.
- **Delayed Feedback for Students:** Students typically wait 3 to 7 days to receive graded homework, missing the critical window to address conceptual misunderstandings before moving on to subsequent topics. Furthermore, students lack systematic visibility into recurring patterns in their mistakes over time.
- **Limitations of Generic Conversational AI (e.g., ChatGPT / Claude / Gemini):**
  - *Lack of Long-term State & Memory:* Generic chatbots have no persistent database tracking individual student progress or longitudinal learning curves.
  - *Absence of End-to-End Automation:* Tutors are forced to manually copy-paste prompts, rubrics, and images one by one.
  - *Grading Inconsistency & High Token Costs:* Free-form text prompts produce variable grading criteria between different runs and incur unsustainable API costs when processing large batches of high-resolution images.

---

## 2. Proposed Solution

This proposal designs a lightweight **Mobile Web Learning Management System (LMS)** that centers on **Multimodal Document Processing** and **Structured Retrieval-Augmented Generation (RAG)**:

1. **Student Experience (Frictionless Ingestion):**
   - Students simply photograph their handwritten homework papers using any mobile web browser without manual data entry.
2. **Core Intelligent Processing Pipeline:**
   - **Document Parsing:** The system performs image dewarping, layout analysis, Vietnamese handwriting recognition, and formula extraction into standardized LaTeX notation.
   - **Rubric Matching:** Automatically retrieves the corresponding assignment prompt, solution barem, and step-by-step scoring criteria established by the tutor.
   - **Step-by-Step Logic Verification:** Assesses each mathematical step for deductive validity against the rubric, pinpointing the exact line where logical errors occur.
   - **Persistent Mistake Profiling:** Catalogs structured mistake taxonomies into a student knowledge graph.
3. **Parent & Tutor Delivery (Automated Evidence-based Reports):**
   - Automatically generates structured reports delivered via automated messaging channels (e.g., Zalo API, SMS).
   - Reports include high-level competency indicators paired with **cropped visual evidence** directly highlighting the error zones from the student's physical submission.

---

## 3. Key Technical Pillars

```
+-------------------+      +-------------------------+      +--------------------------+
|  Handwritten Raw  | ---> |   Multimodal Parsing    | ---> |  Hierarchical Retrieval  |
|  Submission (Img) |      | (Layout & LaTeX OCR)    |      | (Assignment & Mistake DB)|
+-------------------+      +-------------------------+      +--------------------------+
                                                                         |
                                                                         v
+-------------------+      +-------------------------+      +--------------------------+
| Visual Diagnostic | <--- |   Semantic Caching &    | <--- |  Deterministic Grading   |
|   Parent Report   |      | Async Processing Queue  |      |   (Strict JSON Schema)   |
+-------------------+      +-------------------------+      +--------------------------+
```

### 3.1. Multimodal Ingestion & Handwritten OCR
- Combines modern vision-language models with targeted image preprocessing (binarization, perspective correction, contrast enhancement).
- Accurately decomposes mixed-mode layouts: natural Vietnamese handwriting, tabular calculations, diagrams, and mathematical symbols mapped cleanly into LaTeX strings.

### 3.2. Hierarchical Retrieval (Two-Tier RAG)
- **Tier 1 (Assignment & Rubric Indexing):** Uses Hybrid Search (combining Dense Vector embeddings with BM25 keyword matching) to instantly map submitted problem fragments to the tutor's official problem repository and scoring matrix.
- **Tier 2 (Historical Error Profiling):** Retrieves historical error logs specific to that student, conditioning the reasoning prompt to generate deeply contextualized, constructive feedback targeting the student's specific learning blind spots.

### 3.3. Step-by-Step Reasoning & Deterministic Grading
- Enforces structured Chain-of-Thought (CoT) prompts to verify intermediate calculation steps sequentially.
- Applies **Strict JSON Schema Enforcement (Structured Outputs)** to ensure outputs strictly adhere to a deterministic contract: `{step_id, status: pass/fail, error_category, partial_credit, feedback}`. This eliminates hallucinated scoring and guarantees parity across all submissions.

### 3.4. Automated Evidence-based Visual Reporting
- Calculates bounding box coordinates of identified errors on the original submission images.
- Automatically crops and embeds high-resolution snippet callouts into parent reports, providing incontrovertible transparency into student performance.

### 3.5. System Optimization & Semantic Caching
- **Asynchronous Task Queue:** Employs an async job broker (e.g., Redis/Celery) to absorb deadline traffic surges without UI degradation.
- **Semantic Caching:** Caches intermediate embeddings and grading decisions for common correct derivations and frequent canonical error patterns. This strategy reduces redundant inference calls, **cutting recurring API token costs by 60% to 80%** and ensuring operational economic viability.

---

## 4. Value Proposition

1. **80% Reduction in Administrative Load:** Completely automates submission collection, preliminary rubric grading, gradebook calculation, and personalized parent messaging.
2. **Elevated Pedagogical Impact:** Delivers instant, actionable feedback to students within minutes of submission; provides parents with objective, metric-backed visibility into learning progress.
3. **Sustainable Operational Unit Economics:** Semantic caching and asynchronous batching make intelligent multimodal grading economically practical for micro-education businesses.

---

## 5. Independent Thinking & Meaningful Differences from Group Project

In compliance with the assignment guidelines, this individual proposal demonstrates clear independent thinking and explores a completely distinct technological and domain direction compared to the collaborative group project:

| Evaluation Dimension | Group Project (`cs252-final-project`) | Individual Proposal (This Document) |
| :--- | :--- | :--- |
| **Problem Domain** | Systems software / Desktop utility application. | Educational Technology (EdTech) & Intelligent Workflow Automation. |
| **Primary Audience** | Single-user desktop operators / System administrators. | Tri-party educational ecosystem: Private tutors, K-12 students, and parents. |
| **Core Architecture** | C++ Object-Oriented Programming, clean design patterns, and local algorithmic computing. | Distributed Web/Mobile architecture integrating Vision OCR, Hierarchical RAG, and Strict JSON Schema decoding. |
| **Key Technical Innovation** | High-performance C++ class hierarchy and memory management. | Token cost optimization via Semantic Caching, handwritten LaTeX parsing, and evidence-cropped automated reporting. |

This proposal establishes a self-contained, end-to-end conceptual and architectural blueprint addressing a tangible educational challenge through practical computational thinking.
