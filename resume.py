from fpdf import FPDF

class ResumeGenerator:
    def __init__(self, name, contact, summary, skills, experience, education):
        self.name = name
        self.contact = contact
        self.summary = summary
        self.skills = skills
        self.experience = experience
        self.education = education
        self.pdf = FPDF()

    def create_pdf(self):
        self.pdf.add_page()

        # Title - Name
        self.pdf.set_font("Arial", "B", 24)
        self.pdf.cell(200, 10, self.name, ln=True, align="C")
        
        # Contact Info
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, f"Contact: {self.contact}", ln=True, align="C")
        
        # Summary Section
        self.pdf.ln(10)
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, "Summary", ln=True, align="L")
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, self.summary)
        
        # Skills Section
        self.pdf.ln(5)
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, "Skills", ln=True, align="L")
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, self.skills)
        
        # Experience Section
        self.pdf.ln(5)
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, "Experience", ln=True, align="L")
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, self.experience)
        
        # Education Section
        self.pdf.ln(5)
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, "Education", ln=True, align="L")
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, self.education)
        
        # Save the resume as a PDF
        self.pdf.output("resume.pdf")
        print("Resume generated successfully!")

# User input for resume details
name = input("Enter your name: ")
contact = input("Enter your contact info (email/phone): ")
summary = input("Write a short summary about yourself: ")
skills = input("Enter your skills (comma separated): ")
experience = input("Describe your work experience: ")
education = input("Describe your education background: ")

# Create Resume
resume = ResumeGenerator(name, contact, summary, skills, experience, education)
resume.create_pdf()