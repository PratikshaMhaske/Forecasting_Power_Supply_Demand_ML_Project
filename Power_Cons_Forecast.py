import streamlit as st
import pickle
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="Electricity Demand Forecasting",
    page_icon="⚡",
    layout="wide"
)

# Load Model
@st.cache_resource
def load_model():
    with open("prophet_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# Title
st.title("⚡ Electricity Demand Forecasting using Prophet")
st.markdown("Forecast future PJMW power consumption using the trained Prophet model.")

# Sidebar
st.sidebar.header("Forecast Settings")

days = st.sidebar.slider(
    "Select Forecast Horizon (Days)",
    min_value=1,
    max_value=30,
    value=7
)

# Forecast Button
if st.button("Generate Forecast"):

    # Create Future Dates
    future = model.make_future_dataframe(
        periods=days * 24,
        freq='h'
    )

    # Predict
    forecast = model.predict(future)

    # Future Forecast Only
    future_forecast = forecast[
        ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
    ].tail(days * 24)

    st.success(f"Forecast generated for next {days} days.")

    # Forecast Table
    st.subheader("Forecast Values")

    st.dataframe(
        future_forecast,
        use_container_width=True
    )

    # Plot Forecast
    st.subheader("Forecast Trend")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=future_forecast['ds'],
            y=future_forecast['yhat'],
            mode='lines',
            name='Forecast'
        )
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Power Consumption (MW)",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Download CSV
    csv = future_forecast.to_csv(index=False)

    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name=f"forecast_{days}_days.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.markdown(
    "Developed using Prophet Time Series Forecasting Model"
)
