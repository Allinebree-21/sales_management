import pandas as pd
from prophet import Prophet
from datetime import timedelta

def predict_sales(sales_queryset, periods=30):
    """Predict future sales for the next given number of days."""
    if not sales_queryset.exists():
        return None

    df = pd.DataFrame(list(sales_queryset.values('date', 'quantity')))
    df = df.groupby('date')['quantity'].sum().reset_index()
    df.columns = ['ds', 'y']  # Prophet expects these column names

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    # Return recent and predicted data
    result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
    return result
