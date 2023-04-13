# to run the app : streamlit run app.py
# to have the correct version  : pipreqs --encoding=utf8 --force

from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Profil_picture.png"


# --- GENERAL SETTINGS ---s
PAGE_TITLE = "Digital CV | Léo Dujourd'hui"
PAGE_ICON = ":wave:"
NAME = "Léo Dujourd'hui"

PROFESSION = """
 **DATA SCIENTIST / ANALYST**
"""
DESCRIPTION = """
 I work with data to solve business problems or create new solutions, using tools like SQL, R, Python, machine learning, and artificial intelligence.
 """


EMAIL = "leo.dujourdhui@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/leo-dujourd-hui/",
    "GitHub": "https://github.com/le-cmyk",
}

from Projects import PROJECTS



st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="centered",#"wide", "centered", or "wide+fuller"
    initial_sidebar_state="collapsed",
)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(PROFESSION)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Profile ---
st.write('\n')
st.subheader("Profile")
st.write(
    """
Passionate about new technologies, I started learning Python
(self-taught) at the age of 15. Since then, I have never stopped 
learning.
"""
)



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Tensorflow), SQL, C#, R studio
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees, deep neural network
- 🗄️ Databases: MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | Exness – Trading Platforms**")
st.write("09/2022 – 04/2023")
st.write(
    """
    In team with financial engineer
- ► Development of an analysis tool to understand and visualize the evolution of their portfolio.
- ► Analysis of the entry and exit of a high frequency trading robot to improve its performance.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Head of the AI & Data department | Kryptosphere® – Association to democratize web3**")
st.write("09/2022 - Present")
st.write(
    """
- ► Manage a team to complete several projects such as strengthening a DEFI strategy or building a trust indicator.
- ► Leads weekly workshops with students and/or companies in order to democratize techniques around data.
"""
)


# --- JOB 3
st.write('\n')
st.write("🚧", "**Math and informatic teacher | Acadomia - Private lessons and tutoring**")
st.write("11/2021 - Present")
st.write(
    """
- ► Tutored students from middle schools up to university students in math and computer science courses.
- ► Prepared students for university entry exam such as the French “BAC”.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Landscaper | Puthod - Development of green space**")
st.write("06/2017 - 08/2017")
st.write(
    """
- ► Maintenance and creation of green areas with a non-French speaking team.
"""
)


# --- Leadership and activities 
st.write('\n')
st.subheader("Leadership & Activities")
st.write("---")
st.write(
    """
- •  Head of the AI & Data department at Kryptosphere® (2022-2023)
- •  Instructor of whitewater kayaking since 2019
- •  Participated in three hackathons
- •  Volunteer in sports events
- •  Enjoys following new technologies, Space and Astronomy News, and Mixed Martial Arts (MMA)
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")





