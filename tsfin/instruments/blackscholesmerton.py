# Copyright (C) 2016-2018 Lanx Capital Investimentos LTDA.
#
# This file is part of Time Series Finance (tsfin).
#
# Time Series Finance (tsfin) is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# Time Series Finance (tsfin) is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Time Series Finance (tsfin). If not, see <https://www.gnu.org/licenses/>.
"""
A class for modelling Black Scholes Merton
"""
import QuantLib as ql
import numpy as np
from collections import OrderedDict
from tsfin.base import to_ql_date, to_datetime, to_ql_quote_handle


class BlackScholesMerton:

    def __init__(self, ts_underlying_collection, yield_curve):
        """ Model for the Black Scholes Merton model used to evaluate options.

        :param ts_underlying_collection:
            The timeseries of the underlying instruments of the options being calculated.
        :param yield_curve: :py:obj:YieldCurveTimeSeries
            The yield curve of the index rate, used to estimate future cash flows.
        """
        self.ts_underlying = ts_underlying_collection
        self.yield_curve = yield_curve
        self.risk_free_handle = ql.RelinkableYieldTermStructureHandle()
        self.volatility_handle = ql.RelinkableBlackVolTermStructureHandle()
        self.dividend_handle = ql.RelinkableYieldTermStructureHandle()
        self.spot_price_handle = ql.RelinkableQuoteHandle()
        self.bsm_process = ql.BlackScholesMertonProcess(self.spot_price_handle,
                                                        self.dividend_handle,
                                                        self.risk_free_handle,
                                                        self.volatility_handle)
        self.vol_updated = OrderedDict()

    def spot_price_update(self, date, underlying_name, spot_price=None, last_available=True):
        """

        :param date: date-like
            The date.
        :param underlying_name: str
            The underlying Timeseries ts_name
        :param spot_price: float, optional
            An override of the underlying spot price in case you don't wan't to use the timeseries one.
        :param last_available: bool, optional
            Whether to use last available data in case dates are missing in ``quotes``.
        """

        dt_date = to_datetime(date)
        ts_underlying = self.ts_underlying.get(underlying_name).price
        if spot_price is None:
            spot_price = ts_underlying.get_values(index=dt_date, last_available=last_available)
        else:
            spot_price = spot_price

        self.spot_price_handle.linkTo(ql.SimpleQuote(spot_price))

    def dividend_yield_update(self, date, calendar, day_counter, underlying_name, dividend_yield=None, dvd_tax_adjust=1,
                              last_available=True, compounding=ql.Continuous):
        """

        :param date: date-like
            The date.
        :param calendar: QuantLib.Calendar
            The option calendar used to evaluate the model
        :param day_counter: QuantLib.DayCounter
            The option day count used to evaluate the model
        :param underlying_name: str
            The timeseries ts_name used to query the stored timeseries in self.ts_underlying
        :param dividend_yield: float, optional
            An override of the dividend yield in case you don't wan't to use the timeseries one.
        :param dvd_tax_adjust: float, default=1
            The multiplier used to adjust for dividend tax. For example, US dividend taxes are 30% so you pass 0.7.
        :param last_available: bool, optional
            Whether to use last available data in case dates are missing in ``quotes``.
        :param compounding: QuantLib.Compounding, default=Continuous
            The compounding used to interpolate the curve.
        """
        dt_date = to_datetime(date)
        dvd_ts = self.ts_underlying.get(underlying_name).eqy_dvd_yld_12m
        if dividend_yield is None:
            dividend_yield = dvd_ts.get_values(index=dt_date, last_available=last_available)
        else:
            dividend_yield = dividend_yield

        dividend_yield = dividend_yield * dvd_tax_adjust
        dividend = ql.FlatForward(0, calendar, to_ql_quote_handle(dividend_yield), day_counter, compounding)
        self.dividend_handle.linkTo(dividend)

    def yield_curve_update(self, date, calendar, day_counter, maturity, risk_free=None, compounding=ql.Continuous,
                           frequency=ql.Once):
        """

        :param date: date-like
            The date.
        :param calendar: QuantLib.Calendar
            The option calendar used to evaluate the model
        :param day_counter: QuantLib.DayCounter
            The option day count used to evaluate the model
        :param maturity: date-like
            The option maturity.
        :param risk_free: float, optional
            An override of the zero rate in case you don't wan't to use the yield curve implied one.
        :param compounding: QuantLib.Compounding, default=Continuous
            The compounding used to interpolate the curve.
        :param frequency: QuantLib.Frequency, default = Once
            The frequency of the quoted yield.
        """

        ql_date = to_ql_date(date)
        mat_date = to_ql_date(maturity)
        if risk_free is not None:
            zero_rate = risk_free
        else:
            zero_rate = self.yield_curve.zero_rate_to_date(date=ql_date, to_date=mat_date, compounding=compounding,
                                                           frequency=frequency)
        yield_curve = ql.FlatForward(0, calendar, to_ql_quote_handle(zero_rate), day_counter, compounding)
        self.risk_free_handle.linkTo(yield_curve)

    def volatility_update(self, date, calendar, day_counter, ts_option, underlying_name, vol_value=None,
                          last_available=False):

        """

        :param date: date-like
            The date.
        :param calendar: QuantLib.Calendar
            The option calendar used to evaluate the model
        :param day_counter: QuantLib.DayCounter
            The option day count used to evaluate the model
        :param ts_option: py:class:`TimeSeries`
            The option Timeseries.
        :param underlying_name:
            The underlying Timeseries ts_name
        :param vol_value: float, optional
            An override of the volatility value in case you don't wan't to use the timeseries one.
        :param last_available:  bool, optional
            Whether to use last available data in case dates are missing in ``quotes``.
        :return:
        """
        dt_date = to_datetime(date)
        vol_updated = True

        if vol_value is not None:
            volatility_value = vol_value
        else:
            volatility_value = ts_option.ivol_mid.get_values(index=dt_date, last_available=last_available)
            if np.isnan(volatility_value):
                volatility_value = 0
                vol_updated = False

        back_constant_vol = ql.BlackConstantVol(0, calendar, to_ql_quote_handle(volatility_value), day_counter)
        self.volatility_handle.linkTo(back_constant_vol)
        self.vol_updated[underlying_name][to_ql_date(date)] = vol_updated

    def update_process(self, date, calendar, day_counter, ts_option, maturity, underlying_name,
                       vol_last_available=False, dvd_tax_adjust=1, last_available=True, **kwargs):
        """

        :param date: date-like
            The date.
        :param calendar: QuantLib.Calendar
            The option calendar used to evaluate the model
        :param day_counter: QuantLib.DayCounter
            The option day count used to evaluate the model
        :param ts_option: py:class:`TimeSeries`
            The option Timeseries.
        :param maturity: date-like
            The option maturity.
        :param underlying_name:
            The underlying Timeseries ts_name
        :param vol_last_available: bool, optional
            Whether to use last available volatility data in case dates are missing in ``quotes``.
        :param dvd_tax_adjust: float, default=1
            The multiplier used to adjust for dividend tax. For example, US dividend taxes are 30% so you pass 0.7.
        :param last_available: bool, optional
            Whether to use last available data in case dates are missing in ``quotes``.
        :return: bool
            Return True if the volatility timeseries was updated.
        """
        self.vol_updated[underlying_name] = OrderedDict()
        if to_ql_date(date) in self.vol_updated[underlying_name].keys():
            vol_updated = self.vol_updated[underlying_name][to_ql_date(date)]
        else:
            vol_updated = False

        if vol_updated:
            return self.vol_updated[underlying_name][to_ql_date(date)]
        else:
            self.spot_price_update(date=date, underlying_name=underlying_name, last_available=last_available)

            self.dividend_yield_update(date=date, calendar=calendar, day_counter=day_counter,
                                       underlying_name=underlying_name, dvd_tax_adjust=dvd_tax_adjust,
                                       last_available=last_available)

            self.yield_curve_update(date=date, calendar=calendar, day_counter=day_counter, maturity=maturity, **kwargs)

            self.volatility_update(date=date, calendar=calendar, day_counter=day_counter, ts_option=ts_option,
                                   underlying_name=underlying_name, last_available=vol_last_available)

            return self.vol_updated[underlying_name][to_ql_date(date)]
