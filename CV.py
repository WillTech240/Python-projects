from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_sidebar_cv():
    # ==== USER INPUT ====
    name = input("Enter your full name: ")
    title = input("Enter your professional title: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    # Languages
    print("\nEnter your languages (type 'done' when finished):")
    languages = []
    while True:
        lang = input("Language: ")
        if lang.lower() == "done":
            break
        languages.append(lang)

    # References
    print("\nEnter references (type 'done' when finished):")
    references = []
    while True:
        ref = input("Reference (Name - Job Title - Contact): ")
        if ref.lower() == "done":
            break
        references.append(ref)

    hobbies = input("Enter your hobbies (comma separated): ")

    # Profile
    profile = input("Enter your profile summary: ")

    # Education
    print("\nEnter your education details (type 'done' when finished):")
    education = []
    while True:
        edu = input("Education: ")
        if edu.lower() == "done":
            break
        education.append(edu)

    # Experience
    print("\nEnter your work experiences (type 'done' when finished):")
    experiences = []
    while True:
        exp = input("Experience: ")
        if exp.lower() == "done":
            break
        experiences.append(exp)

    # Skills
    print("\nEnter your skills (type 'done' when finished):")
    skills = []
    while True:
        skill = input("Skill: ")
        if skill.lower() == "done":
            break
        skills.append(skill)

    # ==== PDF CREATION ====
    file_name = name.replace(" ", "_") + "_CV.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    # Custom Styles
    header_style = ParagraphStyle("Header", fontSize=22, textColor=colors.HexColor("#154360"),
                                  alignment=1, spaceAfter=10)
    subheader_style = ParagraphStyle("SubHeader", fontSize=12, textColor=colors.HexColor("#1A5276"),
                                     spaceAfter=6, underlineWidth=1)
    body_style = ParagraphStyle("Body", fontSize=10, leading=13, textColor=colors.black)

    # ==== LEFT SIDEBAR ====
    left_content = []
    left_content.append(Paragraph(f"<b>CONTACT</b>", subheader_style))
    left_content.append(Paragraph(f"{email}<br/>{phone}<br/>{address}", body_style))
    left_content.append(Spacer(1, 12))

    if languages:
        left_content.append(Paragraph(f"<b>LANGUAGES</b>", subheader_style))
        for lang in languages:
            left_content.append(Paragraph(f"• {lang}", body_style))
        left_content.append(Spacer(1, 12))

    if references:
        left_content.append(Paragraph(f"<b>REFERENCES</b>", subheader_style))
        for ref in references:
            left_content.append(Paragraph(f"{ref}", body_style))
        left_content.append(Spacer(1, 12))

    if hobbies:
        left_content.append(Paragraph(f"<b>HOBBIES</b>", subheader_style))
        left_content.append(Paragraph(hobbies, body_style))
        left_content.append(Spacer(1, 12))

    # ==== MAIN CONTENT ====
    right_content = []
    right_content.append(Paragraph(f"<b>{name}</b>", header_style))
    right_content.append(Paragraph(f"{title}", subheader_style))
    right_content.append(Spacer(1, 12))

    # Profile
    right_content.append(Paragraph(f"<b>PROFILE</b>", subheader_style))
    right_content.append(Paragraph(profile, body_style))
    right_content.append(Spacer(1, 12))

    # Education
    if education:
        right_content.append(Paragraph(f"<b>EDUCATION</b>", subheader_style))
        for edu in education:
            right_content.append(Paragraph(f"• {edu}", body_style))
        right_content.append(Spacer(1, 12))

    # Experience
    if experiences:
        right_content.append(Paragraph(f"<b>EXPERIENCE</b>", subheader_style))
        for exp in experiences:
            right_content.append(Paragraph(f"• {exp}", body_style))
        right_content.append(Spacer(1, 12))

    # Skills
    if skills:
        right_content.append(Paragraph(f"<b>SKILLS</b>", subheader_style))
        skill_data = [skills[i:i+3] for i in range(0, len(skills), 3)]
        skill_table = Table(skill_data, colWidths=[150, 150, 150])
        skill_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#D6EAF8")),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor("#154360")),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#2E86C1")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#2E86C1")),
        ]))
        right_content.append(skill_table)
        right_content.append(Spacer(1, 12))

    # ==== LAYOUT WITH TWO COLUMNS ====
    layout = Table([
        [left_content, right_content]
    ], colWidths=[180, 360])  # Left = 180px, Right = 360px

    layout.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOX', (0, 0), (0, -1), 1, colors.HexColor("#2E86C1")),  # Left border box
    ]))

    # ==== BUILD PDF ====
    doc.build([layout])
    print(f"\n✅ Sidebar CV has been generated successfully as {file_name}")


# Run function
generate_sidebar_cv()
