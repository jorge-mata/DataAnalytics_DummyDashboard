import streamlit as st
import os

def main():
    st.markdown(
        "> **Disclaimer:** All text on this page is unrelated placeholder content to protect confidential information."
    )
    st.title("About Project Nova")
    st.markdown(" ")  # Line break after title

    # Row 1: Image on the right, intro on the left (less margin)
    row1_col1, row1_col2 = st.columns([3, 2], gap="small")
    with row1_col1:
        st.header("Project Overview")
        st.markdown("---")
        st.write("""
        This dashboard demonstrates the capabilities of Project Nova, a technology initiative focused on optimizing resource allocation and operational efficiency. 
        The project leverages advanced analytics to identify patterns and support strategic decision-making across multiple domains.""")
    with row1_col2:
        img_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "img", "project-nova-meta-image.jpg")
        )
        st.image(img_path, use_container_width=True)

    # Row 2: Header left, text right (less margin)
    st.markdown("---")
    row2_col1, row2_col2 = st.columns([1, 3], gap="small")
    with row2_col1:
        st.header("Objective")
    with row2_col2:
        st.write("""
            The primary objective is to enhance operational transparency and provide actionable insights for stakeholders. The project aims to develop robust analytical models that can forecast trends and highlight areas for improvement, ensuring data-driven strategies are at the forefront of organizational growth.
        """)

    # Row 3: Header left, text right (less margin)
    st.markdown("---")
    row3_col1, row3_col2 = st.columns([1, 3], gap="small")
    with row3_col1:
        st.header("Key Benefits")
    with row3_col2:
        st.write("""
            The insights generated from this platform will empower organizations to:
        """)

    # --- Strategic Insights Cards ---
    st.markdown("""
    <style>
    .nx-card-header {
        background-color: #401f71;
        color: white;
        text-align: center;
        padding: 0.6em 0.2em;
        border-radius: 8px 8px 0 0;
        font-weight: 600;
        font-size: 1.05em;
        letter-spacing: 0.5px;
        margin-bottom: 0;
    }
    .nx-card-body {
        border: 1.5px solid #401f71;
        border-top: none;
        border-radius: 0 0 8px 8px;
        background: transparent;
        padding: 1em 0.7em;
        min-height: 120px;
        font-size: 1em;
        margin-bottom: 1.2em;
        color: #401f71;
    }
    @media (prefers-color-scheme: dark) {
        .nx-card-body {
            color: #fff;
            border-color: #a58fff;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    card_titles = [
        "ENHANCED DATA VISIBILITY",
        "PREDICTIVE ANALYTICS",
        "PROCESS AUTOMATION",
        "SCALABLE SOLUTIONS"
    ]
    card_bodies = [
        "Gain comprehensive insights into operational data, enabling informed decision-making. <br> <br>",
        "Utilize predictive models to anticipate trends and proactively address challenges.",
        "Automate repetitive tasks to improve efficiency and reduce manual errors. <br> <br> ",
        "Deploy solutions that adapt to organizational growth and evolving requirements. <br> <br>"
    ]

    card_cols = st.columns(4, gap="large")
    for i in range(4):
        with card_cols[i]:
            st.markdown(f'<div class="nx-card-header">{card_titles[i]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="nx-card-body">{card_bodies[i]}</div>', unsafe_allow_html=True)
    # --- End Strategic Insights Cards ---

    st.markdown("---")

if __name__ == "__main__":
    main()

# This code is for the "About" page in a Streamlit application.