import os
import json
import requests

from dotenv import load_dotenv

from tools import get_weather

from memory import load_memory, save_memory

from prompts import SYSTEM_PROMPT



load_dotenv()



OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


MODEL = "openrouter/free"


OPENROUTER_URL = (
    "https://openrouter.ai/api/v1/chat/completions"
)




#################################
# TOOLS
#################################


TOOLS = [

{
"type":"function",

"function":{

"name":"get_weather",

"description":
"Get current weather information for a city",


"parameters":{

"type":"object",

"properties":{


"city":{

"type":"string",

"description":
"City name"

}

},


"required":[

"city"

]

}

}

}

]





#################################
# TOOL MAPPING
#################################


TOOL_FUNCTIONS = {


"get_weather":

get_weather


}






#################################
# CALL LLM
#################################


def call_llm(messages):


    headers = {


        "Authorization":

        f"Bearer {OPENROUTER_API_KEY}",


        "Content-Type":

        "application/json"


    }



    payload = {


        "model":

        MODEL,


        "messages":

        messages,


        "tools":

        TOOLS

    }




    response = requests.post(

        OPENROUTER_URL,

        headers=headers,

        json=payload

    )



    response.raise_for_status()



    return response.json()








#################################
# RUN TOOL
#################################


def run_tool(tool_call):


    tool_name = (
        tool_call["function"]["name"]
    )


    arguments = json.loads(

        tool_call["function"]["arguments"]

    )



    if tool_name in TOOL_FUNCTIONS:


        result = TOOL_FUNCTIONS[tool_name](**arguments)


        return result



    return "Tool not found"









#################################
# AGENT LOOP
#################################


def agent_loop(user_input):

    # Load memory and filter out any accidental system prompts saved previously
    memory = load_memory()
    memory = [m for m in memory if m.get("role") != "system"]

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(memory)

    user_msg = {
        "role": "user",
        "content": user_input
    }
    messages.append(user_msg)
    memory.append(user_msg)

    response = call_llm(messages)

    assistant_message = (
        response["choices"][0]["message"]
    )

    # TOOL CALL
    if (
        "tool_calls" in assistant_message
        and assistant_message["tool_calls"]
    ):
        for tool_call in assistant_message["tool_calls"]:
            result = run_tool(tool_call)
            
            # Save the result as the assistant's response so memory doesn't break
            memory.append({"role": "assistant", "content": result})
            save_memory(memory)

            return result

    answer = assistant_message.get("content")

    if answer is None:
        return "Unable to answer."

    memory.append({"role": "assistant", "content": answer})
    save_memory(memory)

    return answer











#################################
# MAIN
#################################


if __name__ == "__main__":



    print("======================")


    print(" Weather AI Agent ")


    print("======================")

    print()



    while True:



        user = input(

            "You : "

        )




        if user.lower()=="exit":


            break





        try:



            response = agent_loop(user)



            print(

                "\nAgent:",

                response

            )




        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")
            if e.response is not None:
                print(f"Details: {e.response.text}")
        except Exception as e:
            print("Error:", e)