from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class LLM:

    def llm_summarize(self,message) -> str:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You must summarize the customer problem in 2-3 line. "
                        "If the input is not a problem, reply: "
                        "'I only summarize your the given problems.'"
                    )
                },
                {"role": "user", "content":message},
            ]
        )

        return resp.choices[0].message.content

# Example usage
if __name__ == "__main__":
    llm = LLM()
    print(llm.llm_summarize("My laptop screen flickers when I open Chrome"))
