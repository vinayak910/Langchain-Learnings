````md
# LangChain Runnables – Part 2  
## Runnable Primitives & LangChain Expression Language (LCEL)

---

## Overview

This video continues the discussion on **LangChain Runnables**, with a strong focus on:

- **Runnable Primitives**
- **LangChain Expression Language (LCEL)**

The core idea emphasized is that **understanding Runnables is essential for building complex, flexible, and production-ready AI workflows in LangChain**.

---

## 1. Recap: What Are LangChain Runnables?

LangChain has **standardized almost all its components into Runnables**, including:

- `PromptTemplate`
- LLMs (e.g., Chat models)
- Output Parsers
- Retrievers

### Why this standardization matters
- Every component follows the **same interface**
- Components can be **connected easily**
- Workflows become **modular and flexible**

### The `invoke()` method
- Introduced as a **standard way to execute any Runnable**
- Works uniformly across prompts, models, parsers, and chains

```text
output = runnable.invoke(input)
````

---

## 2. Categories of Runnables

LangChain Runnables are divided into **two main categories**:

---

## 2.1 Task-Specific Runnables

These are **core LangChain components** that have been converted into Runnables.

### Examples

* `PromptTemplate`
* `ChatOpenAI`
* `StringOutputParser`
* Retrievers

### Key characteristics

* Perform a **specific task**
* Act as **building blocks** inside larger workflows
* Usually combined using Runnable Primitives

---

## 2.2 Runnable Primitives (Most Important)

Runnable Primitives are **fundamental workflow connectors**.

### Purpose

* Control **how data flows**
* Combine multiple Runnables into **complex AI pipelines**

### Common Runnable Primitives

* `RunnableSequence`
* `RunnableParallel`
* `RunnablePassthrough`
* `RunnableLambda`
* `RunnableBranch`

The rest of the video focuses on these primitives.

---

## 3. RunnableSequence

### What it does

* Executes Runnables **sequentially**
* Output of one Runnable becomes input of the next

### Mental model

```text
Runnable A → Runnable B → Runnable C
```

### Use cases

* Prompt → LLM → Output Parser
* Generate content → Explain content
* Multi-step reasoning pipelines

### Example from video

* Generate a joke
* Explain the joke
* Built using:

  * `PromptTemplate`
  * `ChatOpenAI`
  * `StringOutputParser`

---

## 4. RunnableParallel

### What it does

* Executes multiple Runnables **in parallel**
* All Runnables receive the **same input**
* Produces a **dictionary of outputs**

### Mental model

```text
            → Runnable 1
Input  →
            → Runnable 2
```

### Output structure

```json
{
  "output_1": "...",
  "output_2": "..."
}
```

### Use cases

* Generate tweet and LinkedIn post simultaneously
* Create summary + keywords
* Answer + explanation

### Example from video

* Input topic
* Generate:

  * Tweet
  * LinkedIn post

---

## 5. RunnablePassthrough

### What it does

* Returns the input **unchanged**
* Does **no processing**

### Why it is useful

* Helps **retain original inputs**
* Commonly used with `RunnableParallel`
* Allows combining transformed data with raw data

### Typical use case

* Keep the original question
* While another branch generates an answer
* Both are used later together

---

## 6. RunnableLambda

### What it does

* Converts **any Python function** into a Runnable

### Why this is powerful

* Allows **custom logic** inside LangChain workflows
* Bridges traditional Python code with LLM pipelines

### Use cases

* Data preprocessing
* Post-processing LLM output
* Counting words
* Logging intermediate results
* Validation logic

### Example from video

* Generate a joke
* Use `RunnableLambda` to count the number of words
* Output both joke and word count

---

## 7. RunnableBranch

### What it does

* Acts like an **if–else statement**
* Executes **only one branch** based on a condition

### Mental model

```text
if condition:
    Branch A
else:
    Branch B
```

### Use cases

* Customer support email routing
* Intent-based responses
* Handling different categories of input

### Example from video

* Different chains for:

  * Customer complaint
  * General inquiry
  * Spam email

---

## 8. LangChain Expression Language (LCEL)

### What is LCEL?

* A **clean syntax** for composing Runnables
* Uses the pipe (`|`) operator

### Example

```python
prompt | model | parser
```

### Benefits

* More readable
* Less boilerplate
* Easier to reason about data flow

---

## 9. Key Takeaways (Very Important)

* LangChain is shifting from **simple chains** to **data-flow-based workflows**
* Runnable Primitives are the **core abstraction**
* Complex AI systems are built by combining:

  * Sequential logic
  * Parallel execution
  * Conditional routing
  * Custom Python logic

> **Understanding Runnable Primitives is essential for building scalable, real-world AI applications using LangChain.**

---

```
```
