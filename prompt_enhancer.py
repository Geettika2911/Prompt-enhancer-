import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")  # Correct usage

# Function to enhance user-provided prompt
def enhance_prompt(role, context, task):
    """
    Enhances the user-provided Role, Context, and Task into a structured prompt.
    """
    enhanced_prompt = (
        f"You are {role}. You are working within the following context: {context}. "
        f"Your primary task is: {task}. "
        "Before responding, always clarify any assumptions that need to be made. "
        "Ensure the response follows this structured format:\n"
        "1. **Clarifying Assumptions**\n"
        "2. **Structured Response Based on Task**\n"
        "3. **Actionable Next Steps (if applicable)**\n"
        "Provide a well-structured, detailed, and precise response."
    )
    return enhanced_prompt

# Streamlit UI
st.title("Prompt Enhancer App")

# User inputs
role = st.text_input("Enter your role:", "You are an experienced Python coder")
context = st.text_area("Enter the context:", "I am a beginner learning to use AI to create apps")
task = st.text_area("Enter the task:", "I want you to create a Python app that takes (Role, Context, and Task) from users, enhances the prompt, and ensures GPT clarifies assumptions before responding.")

# Enhance the prompt on button click
if st.button("Enhance Prompt"):
    enhanced_prompt = enhance_prompt(role, context, task)
    st.text_area("Enhanced Prompt:", enhanced_prompt, height=200)
