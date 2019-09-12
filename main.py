from mercado_bitcoin import DataAPI

resp = DataAPI.day_summary('BTC', 2019, 9, 11).json()
print(json.dumps(resp, indent=2))