# we get detailed doc on topic (ex : linear regression)
# we will generate 2 things 
# 1. NOTES 
# 2. QUIZ (combine and show to user)
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "MiniMaxAI/MiniMax-M2.1",
    max_new_tokens=300,
    temperature=0.1
)

model1 = ChatHuggingFace(llm = llm)


model2 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.2

)

prompt1 = PromptTemplate(
    template = "generate short and simple notes from the following text \n {text} ",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template = "Generate 5 short question answers from the following text \n {text}",
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template ="Merge the provided notes and quiz into a single document \n "
    "notes->{notes} and quiz ->{quiz}",
    input_variables= ["notes", "quiz"]
)

parser = StrOutputParser()

# parallel chain -> runnable parallel 

parallel_chain = RunnableParallel(
    {
        'notes':prompt1 | model1 | parser,
        'quiz': prompt2 | model2 | parser
    }
    )

merge_chain = prompt3 | model2 | parser 

chain = parallel_chain | merge_chain

text = """
## Linear Regression — explained clearly, step by step

![Image](https://bookdown.org/dli/rguide/R-Manual_files/figure-html/unnamed-chunk-181-1.png)

![Image](https://atmos.uw.edu/~robwood/teaching/451/labs/images/xconcepts12.jpg.pagespeed.ic.oYghSsYO4w.jpg)

![Image](https://www.investopedia.com/thmb/00slg02wynhMgnRGGg8yhEYTNSA%3D/1500x0/filters%3Ano_upscale%28%29%3Amax_bytes%28150000%29%3Astrip_icc%28%29/LeastSquaresMethod-4eec23c588ce45ec9a771f1ce3abaf7f.jpg)

![Image](https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2017/05/FLP_bmi_sq.png?resize=576%2C384)

Think of **linear regression** as a very disciplined way of drawing the **best possible straight line** through data so that we can **understand relationships** and **make predictions**.

---

## 1️⃣ What problem does linear regression solve?

You have data like:

* Area of a house → Price
* Hours studied → Marks
* Experience → Salary

You want to answer:

> “If I know **X**, can I reasonably predict **Y**?”

Linear regression says:
👉 *Yes, if the relationship is roughly linear.*

---

## 2️⃣ The core idea (no math fear 😄)

Linear regression assumes this form:

[
y = mx + c
]

Where:

* **x** → input (feature)
* **y** → output (target)
* **m** → slope (how fast y changes when x changes)
* **c** → intercept (value of y when x = 0)

📌 Example:

```
Price = 5000 × Area + 2,00,000
```

This line is your **model**.

---

## 3️⃣ What does “best fit line” actually mean?

You already have real data points.
The line will **not** pass through all points.

So we define *best* as:

> The line that **minimizes the total error** between predicted and actual values.

### Error for one point:

[
error = actual_y - predicted_y
]

### Total error used by linear regression:

[
\textbf{Sum of Squared Errors (SSE)}
]

Why square?

* Removes negative signs
* Penalizes big mistakes more
* Smooth math for optimization

This method is called **Least Squares**.

---

## 4️⃣ How does the model learn `m` and `c`?

Two main ways:

### ✅ Method 1: Closed-form solution (Normal Equation)

Direct math formula:
[
\theta = (X^TX)^{-1}X^Ty
]

Used when:

* Dataset is small
* Features are limited

### ✅ Method 2: Gradient Descent (most important)

Start with random values of `m` and `c`
Then repeatedly:

1. Predict y
2. Calculate error
3. Adjust parameters slightly
4. Repeat until error is minimum

This is **optimization**, not magic.

---

## 5️⃣ Assumptions (very important for exams & interviews)

Linear regression works well **only if these roughly hold**:

1. **Linearity**
   Relationship between X and Y is linear

2. **Independence**
   Data points are independent

3. **Homoscedasticity**
   Error variance is constant

4. **Normality of errors**
   Errors roughly follow normal distribution

5. **No multicollinearity** (for multiple regression)
   Features shouldn’t be highly correlated

⚠️ Violating assumptions → misleading results

---

## 6️⃣ Simple example (intuitive)

| Area (sqft) | Price (Lakh) |
| ----------- | ------------ |
| 800         | 40           |
| 1000        | 50           |
| 1200        | 60           |

The model learns:

```
Price ≈ 0.05 × Area
```

Now:

* Area = 1100
* Predicted price ≈ **55 Lakh**

That’s linear regression in action.

---

## 7️⃣ Types of linear regression

### 🔹 Simple Linear Regression

* One feature
* `y = mx + c`

### 🔹 Multiple Linear Regression

* Many features
* `y = w₁x₁ + w₂x₂ + ... + b`

Example:

```
Price = 4000×Area + 5×Age + 10000×Location + c
```

---

## 8️⃣ How do we judge if the model is good?

* **R² score** → how much variance is explained
* **MSE / RMSE** → average prediction error
* **Residual plots** → assumption checking

📌 High R² + random residuals = good sign

---

## 9️⃣ Where linear regression shines (and fails)

### ✅ Works great when:

* Relationship is roughly linear
* Data is clean & interpretable
* You need explainability

### ❌ Performs poorly when:

* Strong non-linearity
* Complex interactions
* Heavy outliers
      """

chain.get_graph().print_ascii()
result = chain.invoke({"text":text})

print(result)


