import streamlit as st
from main import agent_loop
from memory import load_memory

st.set_page_config(page_title="Weather AI Agent", page_icon="🌤️")

st.title("🌤️ Weather AI Agent")
st.write("Ask me about the weather in any city!")

# Load existing memory for display
memory = load_memory()
display_messages = [m for m in memory if m.get("role") != "system"]

# Render previous conversation
for msg in display_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("E.g., What is the weather like in Paris?"):
    # Render user message
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Show a spinner while the agent thinks
    with st.spinner("Checking the skies..."):
        response = agent_loop(prompt)
        
    # Render agent response
    with st.chat_message("assistant"):
        st.markdown(response)
        
    # Refresh to grab the updated memory.json state if needed
    st.rerun()
