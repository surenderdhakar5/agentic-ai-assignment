from datetime import datetime


def log_tool(tool_name, input_data):

    with open("agent.log", "a") as file:

        file.write(
            f"{datetime.now()} | {tool_name} | {input_data}\n"
        )