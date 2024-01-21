import streamlit as st
from pathlib import Path
from PIL import Image
import streamlit.components.v1 as com


#---path settings---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "legend_atasks.xlsx"
profile_pic = current_dir / "assets" / "profile-pic.png"
profile_pic2 = current_dir / "assets" / "Steven.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "U2 | Best business partner"
PAGE_ICON = ":wave:"
NAME = "由由（U2 Tech Consulting）"
DESCRIPTION =(
     """
**企业价值观**:客户导向 (Customer-Centric)，鼓励创新 (Encourage-Innovation)，精诚合作 (Collaboration)，携员工共同成长.

**愿景定位**:让你的价值更有价值.
"""
)
EMAIL = "企业邮箱@hotmail.com"
SOCIAL_MEDIA = {
   
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
   
}
PROJECTS = {
    "🏆 **Forecast Sales** - Machine Learning model build up to train& forecast telemarketing": "https://www.163.com",
    "🏆 **User Persona** - Build up user persona to identfy telemarketing opportunities": "https://www.163.com",
    "🏆 **P&L BI Dashboard** - Operation P&L monitor across multiple accounts": "https://www.163.com",
    "🏆 **MS Power Platform Automation** - Jidoka initiatives  to improve productivity": "https://www.163.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=":lollipop:")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
profile_pic2 = Image.open(profile_pic2)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.image(profile_pic2, width=230)

# with col3:
st.title(NAME)
st.write(DESCRIPTION)
st.download_button(
        label=" 📄 Download Company Intro",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
st.write("📫", EMAIL)

# with col3:
#     gif_url= ("https://lottie.host/024e28d9-c1e1-4081-a778-c50dea7c774e/GEwO6idrMN.lottie")
#     st.lottie(gif_url, key = "hello lottie")

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---

st.markdown("---")

st.write('\n')
st.subheader("主营范围")


st.write(
    """
- ✔️ call center  
- ✔️ 咨询
- ✔️ 客服
- ✔️ 企业用工对接平台
- ✔️ 培训
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("领先技能")
st.write(
    """
-💯 技术专业知识：

-👩‍💻 业务分析与战略规划：

-📊 项目管理：

-📚 数据分析与挖掘：

-🗄️ 软件开发与定制：

-💯 信息安全与隐私保护：

-👩‍💻 用户体验设计：

-📊 沟通与协作：

-📚 培训与支持：

-🗄️ 持续学习与创新：
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("主要技能描述")
st.write("---")

# --- JOB 1
st.write("🌊", "**技术专业知识**")
st.write(
    """
深刻理解各种技术领域，包括信息技术、软件开发、数据分析、人工智能、物联网等。
对新兴技术的了解，如区块链、云计算、大数据等。

"""
)

# --- JOB 2
st.write('\n')
st.write("🌊", "**业务分析与战略规划：**")

st.write(
    """
能够理解客户业务需求，分析业务流程，提出优化方案。
制定战略规划，为客户提供可持续的技术解决方案。


"""
)

# --- JOB 3
st.write('\n')
st.write("🌊", "**项目管理：**")

st.write(
    """
具备项目管理技能，能够规划、执行和监控复杂的科技项目。
熟悉敏捷开发、Scrum等项目管理方法论。

"""
)



# --- JOB 5
st.write('\n')
st.write("🍦", "**数据分析与挖掘：**")

st.write(
    """
通过数据分析提供业务洞察，支持决策制定。
使用数据挖掘技术发现潜在的业务机会和问题。

"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"{project}")

# com.ifream("https://lottie.host/daa2ff61-a416-4325-b2a2-7ac9cf77c3b7/PivBztEL6g.lottie")

# --- EDUCATION
st.write('\n')
st.subheader( "**其他背书**")

st.write(
"""
XXXX
XXXX
XXX
XXXXXXXXXX
XXXXXXXX
XXXXXXXXX
"""    
)
