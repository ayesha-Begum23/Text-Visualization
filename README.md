# Text to Mermaid Mindmap Converter

This project is a Streamlit web application that converts user-inputted text into a **Mermaid mindmap** and renders it dynamically. It allows users to visualize their ideas in a structured mindmap format and provides the Mermaid syntax for further use.

## Features
- Converts plain text into **Mermaid mindmap syntax**.
- Renders the Mermaid mindmap dynamically within a Streamlit app.
- Provides an option to copy the generated **Mermaid syntax** for external use.
- Simple and lightweight web-based solution.

---

## Project Architecture

### 1. **User Input**
- Users enter their ideas or concepts as plain text.

### 2. **Text Processing**
- The input text is split into sentences to form hierarchical nodes.
- Each sentence is formatted and structured in **Mermaid mindmap syntax**.

### 3. **Mindmap Generation**
- The converted **Mermaid syntax** is embedded into an HTML template.
- Mermaid.js is used for rendering the mindmap dynamically.

### 4. **Output Display**
- The rendered **Mermaid mindmap** is displayed in the Streamlit interface.
- The generated Mermaid syntax is provided for copying and further customization.

---

## Prerequisites

### **Software Requirements:**
- Python 3.7 or later
- Streamlit framework

### **Python Libraries:**
Install the required dependencies using:

```bash
pip install streamlit
```

---

## How to Run

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### **Step 2: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 3: Run the Streamlit App**

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## Deployment on GitHub Pages or Streamlit Cloud

### **Option 1: Deploy on Streamlit Cloud**
1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository and deploy the app.

### **Option 2: Deploy on a Cloud Server**
- Deploy the app on **Heroku**, **AWS**, or **Google Cloud** using Docker or a virtual environment.

---

## Example Command to Run

```bash
streamlit run app.py
```

---

## Project Structure

```
project-folder/
|-- app.py                  # Main Streamlit app script
|-- README.md               # Documentation file
|-- requirements.txt        # Dependencies file
```

---

## Additional Notes
- **Error Handling:** The script includes exception handling for invalid input.
- **Mermaid.js Integration:** Ensures correct syntax conversion and rendering.

---

## Future Enhancements
- Allow users to customize mindmap styles and themes.
- Add support for hierarchical and nested structures.
- Enable downloading of the generated mindmap as an image or PDF.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

