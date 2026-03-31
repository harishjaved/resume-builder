import streamlit as st

st.set_page_config(page_title="Professional Resume Builder", layout="centered")

# ---------- STYLE ----------
st.markdown("""
<style>
.resume {
    background-color: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    font-family: Arial;
}
.name {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
}
.contact {
    text-align: center;
    font-size: 14px;
    margin-bottom: 20px;
}
.section-title {
    font-size: 18px;
    font-weight: bold;
    margin-top: 20px;
    border-bottom: 2px solid black;
}
.logo {
    display: flex;
    justify-content: center;
    margin-bottom: 15px;
}
a {
    color: blue;
    text-decoration: none;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("📄 Professional Resume Builder")

# ---------- INPUT ----------
st.sidebar.header("Enter Details")

# ✅ LOGO UPLOAD
logo = st.sidebar.file_uploader("Upload Logo / Profile Image", type=["png", "jpg", "jpeg"])

name = st.sidebar.text_input("Full Name")
email = st.sidebar.text_input("Email")
phone = st.sidebar.text_input("Phone")
location = st.sidebar.text_input("Location")

github = st.sidebar.text_input("GitHub (paste full link)")
linkedin = st.sidebar.text_input("LinkedIn (paste full link)")

summary = st.sidebar.text_area("Profile Summary")

education = st.sidebar.text_area("Education")
skills = st.sidebar.text_area("Technical Skills")

soft_skills = st.sidebar.text_area("Soft Skills")
experience = st.sidebar.text_area("Experience")
projects = st.sidebar.text_area("Projects")

languages = st.sidebar.text_input("Languages")

# ---------- BUTTON ----------
if st.sidebar.button("Generate Resume"):

    st.markdown('<div class="resume">', unsafe_allow_html=True)

    # ✅ LOGO DISPLAY
    st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
    st.image(logo, width=120)
    st.markdown('</div>', unsafe_allow_html=True)

    # NAME
    st.markdown(f'<div class="name">{name}</div>', unsafe_allow_html=True)

    # CONTACT
    contact_items = []
    if email:
        contact_items.append(email)
    if phone:
        contact_items.append(phone)
    if location:
        contact_items.append(location)

    contact_line1 = " | ".join(contact_items)

    contact_links = []
    if github:
        contact_links.append(f'<a href="{github}" target="_blank">GitHub</a>')
    if linkedin:
        contact_links.append(f'<a href="{linkedin}" target="_blank">LinkedIn</a>')

    contact_line2 = " | ".join(contact_links)

    contact_html = contact_line1
    if contact_line2:
        contact_html += f"<br>{contact_line2}"

    st.markdown(f'<div class="contact">{contact_html}</div>', unsafe_allow_html=True)

    # PROFILE
    st.markdown('<div class="section-title">Profile</div>', unsafe_allow_html=True)
    st.write(summary)

    # EDUCATION
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    st.write(education)

    # TECHNICAL SKILLS
    st.markdown('<div class="section-title">Technical Skills</div>', unsafe_allow_html=True)
    st.write(skills)

    # SOFT SKILLS
    st.markdown('<div class="section-title">Soft Skills</div>', unsafe_allow_html=True)
    st.write(soft_skills)

    # EXPERIENCE
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)
    st.write(experience)

    # PROJECTS
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    st.write(projects)

    # LANGUAGES (LAST)
    st.markdown('<div class="section-title">Languages</div>', unsafe_allow_html=True)
    st.write(languages)

    st.markdown('</div>', unsafe_allow_html=True)

    # DOWNLOAD
    resume_text = f"""
{name}
{email} | {phone} | {location}
GitHub: {github}
LinkedIn: {linkedin}

Profile:
{summary}

Education:
{education}

Technical Skills:
{skills}

Soft Skills:
{soft_skills}

Experience:
{experience}

Projects:
{projects}

Languages:
{languages}
"""

    st.download_button("📥 Download Resume", resume_text, file_name="resume.txt")