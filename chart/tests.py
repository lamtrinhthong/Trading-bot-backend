import os
import django
import pandas as pd
import MetaTrader5 as mt5
from datetime import datetime
from django.test import TestCase
from chart.models.candlestick import Candlestick
from chart.api.mt5_service import Mt5Service

class CandlestickImportTestCase(TestCase):
    def setUp(self):
        # Initialize test data or setup code if needed
        pass

    def test_import_mt5_data(self):
        # Replace with actual test logic

        # Example parameters
        symbol = 'XAUUSDm'
        timeframe = mt5.TIMEFRAME_D1
        number_of_candles = 3000

        # Initialize your MT5 service
        mt5_service = Mt5Service("Exness-MT5Trial7", 124880048, "Trinhthong0?")

        # Connect to the trading account
        mt5_service.connect()

        # Fetch data from MT5 (example, adjust based on your MT5 service implementation)
        df = mt5_service.get_data(symbol, timeframe, number_of_candles)

        # Add 'time_frame' column with constant value 'D1'
        df['time_frame'] = 'D1'

        # Iterate through DataFrame and save to Django model
        for index, row in df.iterrows():
            Candlestick.objects.create(
                date=row['time'],
                open_price=row['open'],
                high_price=row['high'],
                low_price=row['low'],
                close_price=row['close'],
                time_frame=row['time_frame']
            )

        # Assert that at least one Candlestick object is created
        self.assertGreaterEqual(Candlestick.objects.count(), 1)
