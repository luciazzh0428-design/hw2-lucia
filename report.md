## Business Use Case

This project focuses on automating customer support email responses. The target user is a customer support agent in an e-commerce company. The system takes customer messages as input and generates a professional and helpful response. This task is valuable because customer support communication is repetitive, time-consuming, and directly impacts customer satisfaction.

---

## Model Choice

I initially attempted to integrate a real LLM using the Google Gemini API. However, I encountered issues related to API version compatibility and access permissions. Specifically, multiple model configurations resulted in “model not found” errors despite following documentation.

After testing different configurations and reviewing the API behavior, I determined that the issue was due to access limitations rather than implementation errors. As a result, I implemented a rule-based prototype to simulate LLM behavior while preserving the workflow and evaluation process.

---

## Baseline vs Final Design

The initial prompt was very simple: “Write a reply to the customer.” This produced inconsistent and sometimes unclear responses.

In the second version, I added role definition and tone guidance, which improved consistency.

In the final version, I introduced structured rules such as politeness, empathy, clarification, and safe refusal behavior. This significantly improved the quality and reliability of the responses, making them more suitable for real customer support scenarios.

---

## Limitations

The prototype is limited in handling complex or unexpected customer requests. Since it is rule-based, it cannot generalize beyond predefined conditions. In real-world applications, human review would still be necessary, especially for sensitive or ambiguous cases.

---

## Recommendation

I would recommend deploying this workflow only as a support tool for generating first drafts rather than fully automating responses. With proper human oversight, it can improve efficiency and consistency. However, without review mechanisms, it may produce incomplete or inappropriate responses in edge cases.