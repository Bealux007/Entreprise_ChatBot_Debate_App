# import the all necessary libraries

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import io
import streamlit as st
from bots.steve import query_steve
from bots.elon import query_elon
from referee import summarize_and_judge
from dotenv import load_dotenv
import os 

load_dotenv()

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def generate_pdf(chat_history, summary, winner):
    """Generates a structured and clean PDF file with the full debate conversation, summary, and winner."""
    buffer = io.BytesIO()  # Memory buffer for PDF
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Steve Jobs vs Elon Musk Debate")

    # Page setup
    y_position = 750  
    line_height = 16  

    # Title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, y_position, "🗣️ Steve Jobs vs Elon Musk Debate")
    y_position -= 30

    # Debate conversation
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(100, y_position, "💬 Debate Conversation:")
    y_position -= 20
    pdf.setFont("Helvetica", 12)

    for speaker, response in chat_history:
        text_lines = simpleSplit(f"{speaker}: {response}", "Helvetica", 12, 400)
        for line in text_lines:
            pdf.drawString(100, y_position, line)
            y_position -= line_height
            if y_position < 50:  # New page if needed
                pdf.showPage()
                pdf.setFont("Helvetica", 12)
                y_position = 750  

    # Summary
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(100, y_position, "🏆 Debate Summary:")
    y_position -= 20
    pdf.setFont("Helvetica", 12)
    text_lines = simpleSplit(summary, "Helvetica", 12, 400)
    for line in text_lines:
        pdf.drawString(100, y_position, line)
        y_position -= line_height
        if y_position < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y_position = 750  

    # Winner
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(100, y_position, "🥇 Winner:")
    y_position -= 20
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, y_position, winner)

    pdf.save()
    buffer.seek(0)  # Reset buffer position
    return buffer

# Function to handle the debate
def debate():
    user_input = st.text_input("Enter the debate topic:", "Who has contributed more to the greater advancement of Technology in society?")
    
    if st.button("Start Debate"):
        context = ""
        
        for _ in range(25):  # Adjusted to 5 turns for conciseness
            steve_response = query_steve(user_input, context)
            elon_response = query_elon(user_input, context)

            # Store responses in chat history
            st.session_state.chat_history.append(("Steve Jobs", steve_response))
            st.session_state.chat_history.append(("Elon Musk", elon_response))

            # Update context for better continuity
            context = f"Steve: {steve_response}\nElon: {elon_response}"
            user_input = elon_response.split(".")[-1]  # Take last part of Elon's response

            # Display responses in structured format
            st.subheader("💬 Debate Conversation")
            st.write(f"**Steve Jobs' Response:** {steve_response}")
            st.write(f"**Elon Musk's Response:** {elon_response}")

        # ✅ Manual Summary
        summary_text = """
        Both Steve Jobs and Elon Musk debated the impact of technology on society. 
        Steve emphasized user experience, creativity, and ethical considerations, 
        while Elon focused on innovation, sustainability, and expanding human potential. 
        They acknowledged the role of pioneers like Alan Turing and Tim Berners-Lee 
        in shaping modern technology.
        """
        
        st.subheader("🏆 Debate Summary")
        st.write(summary_text)

        # ✅ Auto-generated Winner
        _, winner = summarize_and_judge(st.session_state.chat_history)
        st.subheader("🥇 Winner:")
        st.write("winner")
        # st.write("Elon Musk")


        # ✅ Button to download PDF
        pdf_buffer = generate_pdf(st.session_state.chat_history, summary_text, winner)
        st.download_button(
            label="📄 Download Debate as PDF",
            data=pdf_buffer,
            file_name="Steve_vs_Elon_Debate.pdf",
            mime="application/pdf"
        )

# Main function
def main():
    st.title("🗣️ Steve Jobs vs Elon Musk Debate")
    debate()

if __name__ == "__main__":
    main()
