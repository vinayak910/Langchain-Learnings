Below are **clean, structured notes**, rewritten for **easy copy-paste into a `.txt` file**.
I’ve reorganized ideas, removed repetition, and added clear headings + bullets, while staying faithful to the concepts.

---

# LangChain Runnables – Structured Notes

## 1. Recap: What Are Chains?

Chains are **predefined workflows** in **LangChain** that connect multiple components together.

### Common Types of Chains

* **Sequential Chains** → one step after another
* **Parallel Chains** → multiple steps at the same time
* **Conditional Chains** → logic-based branching

⚠️ Important insight:

> **Chains are not fundamental primitives. They are built using Runnables behind the scenes.**

---

## 2. Why Runnables Were Needed

### 2.1 Rise of LLM-based Applications

After the release of **ChatGPT** and OpenAI APIs in late 2022:

* Massive increase in LLM-based apps
* Developers wanted to build fast and switch models easily

---

### 2.2 Standardizing LLM Interactions (Initial Goal)

Different LLM providers had **different APIs**:

* OpenAI
* Anthropic
* Google
* Mistral

LangChain’s first goal:

* Provide **one unified interface**
* Allow switching LLM providers with **minimal code changes**

This made LangChain popular early on.

---

### 2.3 Realization: LLM Call Is Only a Small Part

LangChain team realized:

> Calling an LLM is only **one small step** in real-world AI apps.

Example: PDF Question Answering App

* Load documents
* Split text
* Generate embeddings
* Store vectors
* Retrieve relevant chunks
* Format prompts
* Call LLM
* Parse output

To handle this, LangChain introduced **many components**:

* Document Loaders
* Text Splitters
* Embedding Models
* Vector Databases
* Retrievers
* Output Parsers
* Memory modules

---

## 3. The Problem with Chains

### 3.1 Explosion of Specialized Chains

To connect components, LangChain introduced many Chains:

* `LLMChain`
* `RetrievalQAChain`
* `ConversationalRetrievalChain`
* etc.

This caused:

* ❌ Large and hard-to-maintain codebase
* ❌ Steep learning curve
* ❌ Confusion about which Chain to use

---

### 3.2 Core Technical Problem (Most Important)

**Components were NOT standardized.**

Each component had **different method names**:

* LLM → `predict()`
* PromptTemplate → `format()`
* Retriever → `get_relevant_documents()`

Because there was:

* ❌ No common interface
  LangChain had to write **custom glue code (Chains)** to connect everything.

This was **not scalable**.

---

## 4. Introduction of Runnables

Runnables were introduced to **standardize everything**.

---

## 5. What Is a Runnable?

### 5.1 Runnable = Unit of Work

A Runnable:

* Takes an **input**
* Processes it
* Returns an **output**

It represents **one logical step** in a workflow.

---

### 5.2 Common Interface (Key Idea)

Every Runnable follows the **same interface**, including:

* `invoke(input)` → single input
* `batch(inputs)` → multiple inputs
* `stream(input)` → streaming output

This applies to:

* LLMs
* Prompts
* Retrievers
* Parsers
* Custom logic

---

### 5.3 Connectable by Design

Because all Runnables follow the same interface:

* Output of one Runnable automatically becomes input to the next
* No custom glue code needed

---

### 5.4 Composability

A sequence of connected Runnables:

* **Is itself a Runnable**

This means:

* Small workflows → bigger workflows
* Bigger workflows → reusable as building blocks

---

### 5.5 Lego Block Analogy

Runnables are like **Lego blocks**:

* Each block has a purpose
* All blocks have the same connectors
* Blocks can be combined freely
* The final structure is also a Lego block

---

## 6. Relationship Between Chains and Runnables

* **Chains are built using Runnables**
* Chains are now just **convenience wrappers**
* Runnables are the **core abstraction**

Modern LangChain encourages:

> **Build workflows directly using Runnables instead of relying on predefined Chains**

---

## 7. Code Motivation (Conceptual)

In the demo:

* Non-standard components like `NakliLLM` and `NakliPromptTemplate`
* Each had different method names
* Hard to connect directly

This demonstrates:

* Why standardization matters
* Why Runnables are necessary

---

## 8. Final One-Line Summary

> **Runnables standardize all LangChain components into a single interface, enabling flexible, composable, and scalable LLM workflows—without an explosion of custom Chains.**

---

If you want, next I can:

* Convert this into **interview-ready explanation**
* Create a **Runnable vs Chain comparison table**
* Walk through **actual Runnable code step-by-step**
* Explain **RunnableSequence, RunnableParallel, RunnableLambda** clearly

Just tell me what you want next.
