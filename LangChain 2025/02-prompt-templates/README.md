# LangChain prompt templates

LangChain's prompt templates are designed to streamline the creation of prompts for language models, ensuring consistency and flexibility in various applications. In version 0.3, LangChain offers several core prompt templates, each tailored to different use cases:

**1. `PromptTemplate`:**

This template is ideal for simple string-based prompts. It utilizes Python's `str.format` syntax, allowing placeholders to be defined within the template. These placeholders are then replaced with actual values during execution.

*Example:*

```python
from langchain_core.prompts import PromptTemplate

# Define the template with placeholders
template = PromptTemplate.from_template("Tell me a {adjective} joke about {topic}.")

# Format the template with actual values
formatted_prompt = template.format(adjective="funny", topic="chickens")
print(formatted_prompt)
```

*Output:*

```
Tell me a funny joke about chickens.
```

This approach ensures that the prompt is dynamically constructed based on the provided inputs. ([python.langchain.com](https://python.langchain.com/v0.1/docs/modules/model_io/prompts/quick_start/?utm_source=chatgpt.com))

**2. `ChatPromptTemplate`:**

For more complex interactions, especially those involving multiple turns in a conversation, the `ChatPromptTemplate` is appropriate. It allows the construction of a sequence of messages, each associated with a specific role, such as system, human, or AI.

*Example:*

```python
from langchain_core.prompts import ChatPromptTemplate

# Define a sequence of messages with roles and content
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant named {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)

# Format the template with actual values
messages = chat_template.format_messages(name="Alice", user_input="Can you tell me a joke?")
for message in messages:
    print(f"{message.role}: {message.content}")
```

*Output:*

```
system: You are a helpful AI assistant named Alice.
human: Hello, how are you doing?
ai: I'm doing well, thanks!
human: Can you tell me a joke?
```

This structure is particularly useful for setting up context in chat-based applications, ensuring that the AI model understands its role and the flow of the conversation. ([python.langchain.com](https://python.langchain.com/v0.1/docs/modules/model_io/prompts/quick_start/?utm_source=chatgpt.com))

**3. `FewShotPromptWithTemplates`:**

When there's a need to provide the model with examples to guide its responses, the `FewShotPromptWithTemplates` comes into play. This template allows the inclusion of multiple examples within the prompt, helping the model understand the desired output format or style.

*Example:*

```python
from langchain_core.prompts import FewShotPromptWithTemplates, PromptTemplate

# Define the example prompt template
example_prompt = PromptTemplate.from_template("Q: {question}\nA: {answer}")

# Define the few-shot prompt with examples
few_shot_prompt = FewShotPromptWithTemplates(
    example_prompt=example_prompt,
    examples=[
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
    ],
    suffix=PromptTemplate.from_template("Q: {input_question}\nA:"),
    input_variables=["input_question"]
)

# Format the prompt with a new question
formatted_prompt = few_shot_prompt.format(input_question="Who wrote '1984'?")
print(formatted_prompt)
```

*Output:*

```
Q: What is the capital of France?
A: Paris

Q: What is 2 + 2?
A: 4

Q: Who wrote '1984'?
A: 
```

By providing these examples, the model is better equipped to generate accurate and contextually relevant responses. ([api.python.langchain.com](https://api.python.langchain.com/en/latest/core/prompts/langchain_core.prompts.few_shot_with_templates.FewShotPromptWithTemplates.html?utm_source=chatgpt.com))

In summary, LangChain's core prompt templates in version 0.3 offer a robust framework for crafting prompts tailored to various scenarios, enhancing the interaction between users and language models. 