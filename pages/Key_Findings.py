import streamlit as st

def main():
    st.markdown(
        "> **Disclaimer:** All text on this page is unrelated placeholder content to protect confidential information."
    )
    st.title("Key Insights")

    st.markdown("""
    This section summarizes the main observations derived from the Project Nova dashboard. The highlights include trends in operational metrics, resource utilization, and early indicators for process optimization. These insights support continuous improvement and strategic planning.

    **Examples of key insights:**
    - **Increase in Resource Utilization**
    - **Improved Process Efficiency**
    - **Average Task Completion Time by Department**
    - **Volume and Frequency by Activity Type**
    - **Error Rates by Process Segment**
    - **Performance Metrics by Quarter**
    """)

    st.markdown("---")
    st.header("Detailed Observations")

    st.markdown("""
    - **Increase in Resource Utilization**  
      There has been a consistent rise in the use of available resources across reporting periods.
                
    - **Improved Process Efficiency**  
      Efficiency metrics show a positive trend, with average completion times decreasing over the last year.

    - **Average Task Completion Time by Department**  
      Certain departments demonstrate faster turnaround times, highlighting best practices for broader adoption.

    - **Volume and Frequency by Activity Type**  
      Routine activities remain the most frequent, while specialized tasks show steady growth.

    - **Error Rates by Process Segment**  
      Segments involving manual intervention exhibit higher error rates, suggesting opportunities for automation.

    - **Performance Metrics by Quarter**  
      Quarterly performance varies, with notable improvements in Q2 and Q4.
    """)

if __name__ == "__main__":
    main()

# This code is for the "Key Insights" page in a Streamlit