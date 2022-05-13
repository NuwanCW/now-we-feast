import json
import requests
from pprint import pprint
from pyinstrument import Profiler

profiler = Profiler()
feature_data = {
    "features": [
      "driver_hourly_stats:conv_rate",
      "driver_hourly_stats:acc_rate",
      "driver_hourly_stats:avg_daily_trips"
    ],
    "entities": {
      "driver_id": [1004, 1005]
    }
}

profiler.start()
resp = requests.post("http://localhost:6566/get-online-features", data=json.dumps(feature_data))
profiler.stop()
profiler.print()
pprint(resp.json())