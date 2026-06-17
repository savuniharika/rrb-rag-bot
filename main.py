from agent import agent

def main():
    print("🤖 Deep Agent Started... (type 'exit' to stop)")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        try:
            response = agent.invoke({
                "messages": [
                    ("user", user_input)
                ]
            })

            last_message = response["messages"][-1]

            if isinstance(last_message.content, list):
                answer = ""

                for item in last_message.content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        answer += item.get("text", "")

                print("\nAgent:", answer)

            else:
                print("\nAgent:", last_message.content)

        except Exception as e:
            print("\nError:", str(e))


if __name__ == "__main__":
    main()