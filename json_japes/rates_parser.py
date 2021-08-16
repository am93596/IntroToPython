import json


class RatesParser:
    def __init__(self, rates_filepath):
        self._open_json_file(rates_filepath)
        self.base = self._rates_info.get("base")
        self.date = self._rates_info.get("date")
        self.rates = self._rates_info.get("rates")
        # self.aud = self.rates.get("AUD")
        # self.gbp = self.rates["GBP"]
        # self.usd = self.rates["USD"]

    def _open_json_file(self, filepath):
        with open(filepath) as rates:
            self._rates_info = json.load(rates)


rp = RatesParser("exchange_rates.json")
# print(rp.aud)
# print(rp._open_json_file('exchange_rates.json'))
