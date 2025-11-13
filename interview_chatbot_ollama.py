import streamlit as st
import subprocess
import json
import textwrap

# ----------------------------- #
#  OLLAMA LLM CALL FUNCTION
# ----------------------------- #
def generate_llm_response(prompt, model="llama3"):
    """
    Calls the local Ollama model and returns its response.
    Requires Ollama to be installed and running.
    """
    try:
        # Use subprocess to call Ollama's CLI and get response as JSON
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return "⚠️ Ollama error: " + result.stderr.strip()
        return result.stdout.strip()

    except Exception as e:
        return f"❌ Error calling Ollama: {e}"

# ----------------------------- #
#  STREAMLIT UI
# ----------------------------- #
st.set_page_config(page_title="Interview & Resume Coach", page_icon="💼", layout="centered")

st.markdown("""
    <h2 style='text-align:center;'>💬 Interview & Resume Coach </h2>
    <p style='text-align:center; color:gray;'>Ask me anything about interviews, resumes, or placements!</p>
""", unsafe_allow_html=True)

# Chat storage
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there! 👋 I'm your Interview & Resume Coach. How can I help you today?"}
    ]

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask me about resumes, interviews, or placements..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response using Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = generate_llm_response(
                f"You are an expert interview and resume coach. "
                f"Answer clearly, give examples, and be professional.\n\nUser: {prompt}\nAI:"
            )
            wrapped = textwrap.fill(response, width=100)
            st.markdown(wrapped)
            st.session_state.messages.append({"role": "assistant", "content": response})
