import json
import google.generativeai as genai

LLM_CACHE = {}

def call_llm(model, prompt):
    if prompt in LLM_CACHE:
        return LLM_CACHE[prompt]

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.4,
                "response_mime_type": "application/json"
            }
        )
        text = response.text.strip()
        LLM_CACHE[prompt] = text
        return text
    except Exception:
        return json.dumps({
            "user_response": "Thank you for your feedback.",
            "summary": "Error generating summary.",
            "recommended_action": "Review manually."
        })


def combined_prompt(rating, review):
    return f"""
You are an AI assistant helping a business analyze customer feedback.

Customer rating: {rating}/5
Customer review: "{review}"

Return a VALID JSON object with EXACTLY these fields:
- user_response
- summary
- recommended_action

Output ONLY JSON.
"""
