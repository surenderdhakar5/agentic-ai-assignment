from agent import run_agent
from tools import get_order

print(get_order("ORD-1001"))

print("🤖 AI Customer Support Agent")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = run_agent(question)

    print("Agent:", answer)