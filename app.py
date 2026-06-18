import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Advanced Page Configurations
st.set_page_config(
    page_title="Enterprise Supply Chain Data Cleaning Automation Pipeline", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏭 Enterprise Data Cleaning & Supply Chain Automation Pipeline")
st.markdown("""
This production-ready pipeline automates data quality engineering for high-throughput supply chain networks.
It ingests messy operational datasets, flags structural anomalies, imputes multi-variate metrics, 
and delivers clean, analytics-ready business intelligence profiles.
""")

# ----------------------------------------------------------------
# ADVANCED DATA ENGINE: GENERATING COMPLICATED INTERACTION DATA
# ----------------------------------------------------------------
@st.cache_data
def generate_complex_enterprise_data():
    np.random.seed(101)
    n_records = 500
    
    # Simulating standard structural columns
    shipment_ids = [f"SHP-{200000 + i}" for i in range(n_records)]
    
    # 1. Messy Continuous Data (Ages / Lead Times)
    lead_times = np.random.choice([2.5, 4.0, np.nan, 12.5, 7.0, -5.0, 48.0, np.nan, 8.5], size=n_records)
    
    # 2. Corrupted Categorical Entries with white-spaces and mixed casing variation
    carrier_variants = ["DHL Global", "dhl global", "FedEx Express", "FEDEX CORP", "  FedEx Express  ", "UPS Logistics", None, "DHL GLOBAL"]
    carriers = np.random.choice(carrier_variants, size=n_records)
    
    # 3. Corrupted Financial Records (Negative costs, structural text symbols, empty properties)
    shipping_costs = np.random.choice([450.0, 1200.50, -250.0, np.nan, 3100.0, 85.25, 0.0, np.nan], size=n_records)
    
    # 4. Regional Categorization
    regions = np.random.choice(["EMEA", "APAC", "LATAM", "NORTHAM"], size=n_records)
    
    df = pd.DataFrame({
        "Shipment_ID": shipment_ids,
        "Carrier_Partner": carriers,
        "Transit_Lead_Days": lead_times,
        "Operational_Cost": shipping_costs,
        "Global_Region": regions
    })
    
    # Explicitly inject identical full rows to create duplicates
    duplicates = df.iloc[15:65].copy()
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # Shuffle indices to mix anomalies throughout the structure
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    return df

# ----------------------------------------------------------------
# SIDEBAR CONTROL PANEL
# ----------------------------------------------------------------
st.sidebar.header("📂 Data Ingestion Interface")
st.sidebar.markdown("Ingest historical logs into the preprocessing framework:")
input_selection = st.sidebar.radio("Data Stream Source:", ("Load Complicated Enterprise Demo Logs", "Upload custom CSV Source"))

if input_selection == "Upload custom CSV Source":
    uploaded_file = st.sidebar.file_uploader("Upload operational CSV target", type=["csv"])
    if uploaded_file is not None:
        raw_dataframe = pd.read_csv(uploaded_file)
    else:
        st.sidebar.warning("Awaiting upload stream. Visualizing enterprise demo profile instead.")
        raw_dataframe = generate_complex_enterprise_data()
else:
    raw_dataframe = generate_complex_enterprise_data()

# ----------------------------------------------------------------
# PRODUCTION CLEANING FRAMEWORK (COMPLEX DATA ENGINEERING LOGIC)
# ----------------------------------------------------------------
def execute_enterprise_cleaning_pipeline(df):
    execution_logs = []
    processed_df = df.copy()
    
    # Pipeline Step 1: Duplicate Validation
    pre_duplicate_count = len(processed_df)
    processed_df.drop_duplicates(inplace=True)
    post_duplicate_count = len(processed_df)
    execution_logs.append(f"✓ **Deduplication Engine:** Dropped **{pre_duplicate_count - post_duplicate_count}** redundant historical snapshot copies.")
    
    # Pipeline Step 2: Text Normalization and Categorical Mapping
    if "Carrier_Partner" in processed_df.columns:
        processed_df["Carrier_Partner"] = processed_df["Carrier_Partner"].astype(str).str.strip().str.upper()
        # Consolidate structural naming fragments
        processed_df["Carrier_Partner"] = processed_df["Carrier_Partner"].replace({
            "DHL GLOBAL": "DHL SUPPLY CHAIN",
            "FEDEX CORP": "FEDEX EXPRESS",
            "NONE": np.nan,
            "NAN": np.nan
        })
        execution_logs.append("✓ **Text Harmonization:** Fixed string casings, stripped structural padding, and consolidated vendor codes.")
        
    # Pipeline Step 3: Outlier and Anomalous Domain Enforcement
    if "Transit_Lead_Days" in processed_df.columns:
        # Flagging extreme physical anomalies (e.g., negative days or unrealistic durations)
        outlier_mask = (processed_df["Transit_Lead_Days"] <= 0) | (processed_df["Transit_Lead_Days"] > 30)
        outlier_count = outlier_mask.sum()
        processed_df.loc[outlier_mask, "Transit_Lead_Days"] = np.nan
        if outlier_count > 0:
            execution_logs.append(f"✓ **Outlier Treatment:** Flagged and isolated **{outlier_count}** anomalous transit day properties (negative periods or extremes).")
            
    if "Operational_Cost" in processed_df.columns:
        invalid_costs = (processed_df["Operational_Cost"] < 0).sum()
        processed_df["Operational_Cost"] = processed_df["Operational_Cost"].mask(processed_df["Operational_Cost"] < 0, np.nan)
        if invalid_costs > 0:
            execution_logs.append(f"✓ **Financial Reconciliation:** Cleared **{invalid_costs}** negative billing errors inside cost vectors.")
            
    # Pipeline Step 4: Multi-Variate Context-Aware Imputation
    missing_map_pre = processed_df.isnull().sum()
    
    for columns in processed_df.columns:
        if processed_df[columns].isnull().sum() > 0:
            if processed_df[columns].dtype in ['float64', 'int64']:
                # Impute missing values with statistical median values
                median_value = processed_df[columns].median()
                processed_df[columns].fillna(median_value, inplace=True)
            else:
                # Fill string cells using mode categorization
                mode_fallback = processed_df[columns].mode()[0] if not processed_df[columns].mode().empty else "UNKNOWN"
                processed_df[columns].fillna(mode_fallback, inplace=True)
                
    execution_logs.append("✓ **Statistical Imputation Engine:** Successfully handled all unresolved missing data matrices using median/mode parameters.")
    
    return processed_df, execution_logs, missing_map_pre

# Execute advanced transformations
cleaned_dataframe, logs, missing_map_pre = execute_enterprise_cleaning_pipeline(raw_dataframe)

# ----------------------------------------------------------------
# STREAMLIT FRONT-END ARCHITECTURE
# ----------------------------------------------------------------
tabs = st.tabs(["📉 Executive Data Integrity Analytics", "⚙️ Pipeline Transformations", "📊 Raw Structural View"])

with tabs[0]:
    st.subheader("📋 Executive Performance Summary Metrics")
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    
    with kpi_col1:
        st.metric(label="Raw Records Evaluated", value=f"{raw_dataframe.shape[0]} rows")
    with kpi_col2:
        st.metric(label="Cleaned Production Matrix Size", value=f"{cleaned_dataframe.shape[0]} rows")
    with kpi_col3:
        total_nulls_remedied = missing_map_pre.sum()
        st.metric(label="Resolved Null Cells", value=int(total_nulls_remedied), delta="Pipeline Cleaned", delta_color="normal")
        
    st.write("---")
    
    ui_left, ui_right = st.columns([1, 1])
    
    with ui_left:
        st.subheader("💡 Cleaned Output Preview")
        st.dataframe(cleaned_dataframe.head(12), use_container_width=True)
        
        # Download pipeline results
        buffer = io.StringIO()
        cleaned_dataframe.to_csv(buffer, index=False)
        st.download_button(
            label="💾 Export Cleaned Enterprise Dataset (CSV)",
            data=buffer.getvalue(),
            file_name="cleaned_enterprise_supply_chain_report.csv",
            mime="text/csv"
        )
        
    with ui_right:
        st.subheader("📈 Operational Financial Profiles by Vendor and Region")
        sns.set_theme(style="whitegrid")
        fig, ax = plt.subplots(figsize=(8, 4.8))
        
        # Plot distribution of cost against carrier and global region distribution
        sns.barplot(
            data=cleaned_dataframe,
            x="Carrier_Partner",
            y="Operational_Cost",
            hue="Global_Region",
            palette="muted",
            errorbar=None,
            ax=ax
        )
        ax.set_title("Aggregated Operational Expenditures ($) across Global Regions")
        ax.set_ylabel("Total Financial Allocations ($)")
        ax.set_xlabel("Validated Strategic Logistics Carriers")
        plt.xticks(rotation=10)
        st.pyplot(fig)

with tabs[1]:
    st.subheader("🛠️ Sequence Log Verification Output")
    for pipeline_log in logs:
        st.success(pipeline_log)
        
    st.write("---")
    st.subheader("🗺️ Pre-Transformation Missing Cell Heatmap Profile")
    
    fig_heat, ax_heat = plt.subplots(figsize=(10, 3.5))
    sns.heatmap(raw_dataframe.isnull(), cbar=False, yticklabels=False, cmap="viridis", ax=ax_heat)
    ax_heat.set_title("Density Map Highlight: Null Cell Configurations inside Source Ingestions")
    st.pyplot(fig_heat)

with tabs[2]:
    st.subheader("🔍 Pre-Processed Ingested Audit Data")
    st.dataframe(raw_dataframe, use_container_width=True)