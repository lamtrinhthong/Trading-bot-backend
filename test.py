import os
import django
import pandas as pd
import MetaTrader5 as mt5
from datetime import datetime
from chart.models.candlestick import Candlestick
from chart.api.mt5_service import MT5Service

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading_web_backend.settings')  # Replace with your project's settings module
django.setup()

def import_mt5_data(symbol, timeframe, number_of_candles):
    # Initialize your MT5 service (adjust import path and initialization as per your structure)
    mt5_service = Mt5Service("Exness-MT5Trial7", 124880048, "Trinhthong0?")

    # Fetch data from MT5
    df = mt5_service.get_data(symbol, timeframe, number_of_candles)

    # Save data to Django model
    for index, row in df.iterrows():
        print(row['time'])
        print(row['open'])
        print(row['high'])
        print(row['low'])
        print(row['close'])

        # Candlestick.objects.create(
        #     date=row['time'],
        #     open_price=row['open'],
        #     high_price=row['high'],
        #     low_price=row['low'],
        #     close_price=row['close'],
        #     time_frame=timeframe  # Assuming all data belongs to the same timeframe
        # )

    print('Candlestick data imported successfully')

if __name__ == '__main__':
    symbol = 'XAUUSDm'  # Replace with your desired symbol
    timeframe = mt5.TIMEFRAME_D1   # Replace with your desired timeframe
    number_of_candles = 1000  # Replace with the number of candles to fetch

    import_mt5_data(symbol, timeframe, number_of_candles)
