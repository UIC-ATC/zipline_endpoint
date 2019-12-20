import types
from typing import Optional

import pandas as pd
from flask import Flask, request
from flask_restful import Api, Resource
from zipline import run_algorithm
from zipline.utils.calendars import get_calendar

app = Flask(__name__)
api = Api(app)


class Backtest(Resource):
    def get(self):
        module = types.ModuleType(request.args['name'])

        exec(request.get_data().decode("utf-8"), module.__dict__)

        try:
            trading_calendar = get_calendar(request.args['trading_calendar'])
        except KeyError:
            trading_calendar = None

        results = run_algorithm(
            pd.to_datetime(request.args['start']).tz_localize('US/Eastern'),
            pd.to_datetime(request.args['end']).tz_localize('US/Eastern'),
            module.initialize,
            int(request.args['capital_base']),
            module.__dict__.get('handle_data', None),
            module.__dict__.get('before_trading_start', None),
            module.__dict__.get('analyze', None),
            request.args.get('data_frequency', 'daily'),
            trading_calendar=trading_calendar,
            metrics_set=request.args.get('metrics_set', 'default')
        )

        return results.to_json()


api.add_resource(Backtest, '/backtest')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
