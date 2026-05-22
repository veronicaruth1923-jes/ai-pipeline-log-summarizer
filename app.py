from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_log(log_text):

    prompt = f"""
    You are an AI assistant for Data Engineering and DevOps teams.

    Analyze the following pipeline log and provide:
    1. Failure Summary
    2. Root Cause
    3. Business Impact
    4. Severity
    5. Recommended Actions

    Log:
    {log_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert Data Engineering incident analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    with open("sample_logs/schema_error.log", "r") as file:
        log_data = file.read()

    summary = summarize_log(log_data)

    print("\nAI GENERATED INCIDENT SUMMARY\n")
    print(summary)
