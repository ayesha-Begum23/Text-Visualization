import streamlit as st

def convert_to_mermaid_mindmap(text):
    """
    Converts input text into a Mermaid mindmap syntax.
    """
    # Split the text into sentences for each step
    steps = text.split('. ')
    
    # Initialize the Mermaid mindmap syntax
    mermaid_code = "mindmap\n"
    
    # Add the main node (root)
    mermaid_code += "    root[Root]\n"
    
    # Iterate through sentences and add each as a sub-node
    for i, step in enumerate(steps):
        if step:  # Ensure there's content in the step
            # Clean and format each step for readability in the mindmap
            step = step.strip().capitalize()
            mermaid_code += f"        child{i}[{step}]\n"
    
    return mermaid_code

# Streamlit app setup
st.title("Text to Mermaid Mindmap Converter & Renderer")

# Text area for user input
user_text = st.text_area("Enter your ideas or concepts as text:", height=200)

# Convert and render button
if st.button("Generate Mindmap"):
    # Check if user text is provided
    if user_text.strip():
        # Convert text to Mermaid mindmap syntax
        mermaid_syntax = convert_to_mermaid_mindmap(user_text)
        
        # Prepare the HTML for Mermaid rendering dynamically
        mermaid_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.4.0/mermaid.min.js"></script>
            <script>
                mermaid.initialize({{ startOnLoad: true }});
            </script>
        </head>
        <body>
            <div class="mermaid">
            {mermaid_syntax}
            </div>
        </body>
        </html>
        """
        
        # Render the Mermaid diagram in Streamlit
        st.subheader("Rendered Mermaid Mindmap:")
        st.components.v1.html(mermaid_html, height=500)
        
        # Display Mermaid syntax for copying
        st.subheader("Mermaid Syntax:")
        st.code(mermaid_syntax, language="mermaid")
    else:
        st.error("Please enter some text to convert into a Mermaid mindmap.")
