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
Functions for converting strings to QuantLib objects. Used to map attributes stored in the database to objects.
"""
import pandas as pd
import QuantLib as ql


def to_ql_date(arg):
    """Converts a string, datetime.datetime or numpy.datetime64 instance to ql.Date instance.

    Parameters
    ----------
    arg: date-like

    Returns
    -------
    QuantLib.Date

    """
    if isinstance(arg, ql.Date):
        return arg
    else:
        arg = pd.to_datetime(arg)
        return ql.Date(arg.day, arg.month, arg.year)


def to_ql_frequency(arg):
    """Converts string with a period representing a tenor to a QuantLib period.

    Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.Period

    """

    if arg.upper() == "ANNUAL":
        return ql.Annual
    elif arg.upper() == "SEMIANNUAL":
        return ql.Semiannual
    elif arg.upper() == "QUARTERLY":
        return ql.Quarterly
    elif arg.upper() == "BIMONTHLY":
        return ql.Bimonthly
    elif arg.upper() == "MONTHLY":
        return ql.Monthly
    elif arg.upper() == "AT_MATURITY":
        return ql.Once
    else:
        raise ValueError("Unable to convert {} to a QuantLib frequency".format(arg))


def to_ql_calendar(arg):
    """Converts string with a calendar name to a calendar instance of QuantLib.

    Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.Calendar

    """

    if arg.upper() == "NYSE":
        return ql.UnitedStates(ql.UnitedStates.NYSE)
    if arg.upper() == "US":
        return ql.UnitedStates()
    if arg.upper() == "UK":
        return ql.UnitedKingdom()
    if arg.upper() == "BZ":
        return ql.Brazil()
    if arg.upper() == "TARGET":
        return ql.TARGET()
    if arg.upper() == "FD":
        return ql.UnitedStates(ql.UnitedStates.FederalReserve)
    else:
        raise ValueError("Unable to convert {} to a QuantLib calendar".format(arg))


def to_ql_currency(arg):
    """Converts string with a calendar name to a calendar instance of QuantLib.

    Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.Currency

    """

    if arg.upper() == "USD":
        return ql.USDCurrency()
    if arg.upper() == "BRL":
        return ql.BRLCurrency()
    if arg.upper() == "EUR":
        return ql.EURCurrency()
    else:
        raise ValueError("Unable to convert {} to a QuantLib currency".format(arg))


def to_ql_business_convention(arg):
    """Converts a string with business convention name to the corresponding QuantLib object.

    Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.BusinessConvention

    """

    if arg.upper() == "FOLLOWING":
        return ql.Following
    elif arg.upper() == "MODIFIEDFOLLOWING":
        return ql.ModifiedFollowing
    elif arg.upper() == "UNADJUSTED":
        return ql.Unadjusted
    else:
        raise ValueError("Unable to convert {} to a QuantLib business convention".format(arg))


def to_ql_day_counter(arg):
    """Converts a string with day_counter name to the corresponding QuantLib object.

    Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.DayCounter

    """
    if arg.upper() == "THIRTY360E":
        return ql.Thirty360(ql.Thirty360.European)
    elif arg.upper() == "THIRTY360":
        return ql.Thirty360()
    elif arg.upper() == "ACTUAL360":
        return ql.Actual360()
    elif arg.upper() == "ACTUAL365":
        return ql.Actual365Fixed()
    elif arg.upper() == "ACTUALACTUAL":
        return ql.ActualActual(ql.ActualActual.ISMA)
    elif arg.upper() == "ACTUALACTUALISMA":
        return ql.ActualActual(ql.ActualActual.ISMA)
    elif arg.upper() == "ACTUALACTUALISDA":
        return ql.ActualActual(ql.ActualActual.ISDA)
    elif arg.upper() == "BUSINESS252":
        return ql.Business252()
    else:
        raise ValueError("Unable to convert {} to a QuantLib day counter".format(arg))


def to_ql_date_generation(arg):
    """Converts a string with date_generation name to the corresponding QuantLib object.

    Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.DateGeneration

    """
    if arg.upper() == "FORWARD":
        return ql.DateGeneration.Forward
    elif arg.upper() == "BACKWARD":
        return ql.DateGeneration.Backward
    elif arg.upper() == "CDS20IMM":
        return ql.DateGeneration.TwentiethIMM
    elif arg.upper() == "CDS2015":
        return ql.DateGeneration.CDS2015
    elif arg.upper() == "CDS":
        return ql.DateGeneration.CDS
    else:
        raise ValueError("Unable to convert {} to a QuantLib date generation specification".format(arg))


def to_ql_compounding(arg):
    """Converts a string with compounding convention name to the corresponding QuantLib object.

    # Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.Compounding

    """
    if arg.upper() == "COMPOUNDED":
        return ql.Compounded
    elif arg.upper() == "SIMPLE":
        return ql.Simple
    elif arg.upper() == "CONTINUOUS":
        return ql.Continuous
    else:
        raise ValueError("Unable to convert {} to a QuantLib compounding specification".format(arg))


def to_ql_index(arg):
    """Converts a string with index name to the corresponding QuantLib object.

    Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.Index

    """
    if arg.upper() == "USDLIBOR":
        return ql.USDLibor
    elif arg.upper() == "FEDFUNDS":
        return ql.FedFunds()
    else:
        raise ValueError("Unable to convert {} to a QuantLib index".format(arg))


def to_ql_overnight_index(arg):
    """Converts a string with overnight index name to the corresponding QuantLib object.

    Parameters
    ----------
    arg: str

    Returns
    -------
    QuantLib.OvernightIndex

    """
    if arg.upper() == "FEDFUNDS":
        return ql.FedFunds()
    else:
        raise ValueError("Unable to convert {} to a QuantLib overnight index".format(arg))


def to_ql_option_type(arg):

    if arg.upper() == 'CALL':
        return ql.Option.Call
    elif arg.upper() == 'PUT':
        return ql.Option.Put


def to_ql_rate_index(arg, *args):
    """Converts a string with index name to the corresponding QuantLib object.

    Parameters
    ----------
    arg: str
    arg2: ql.Period

    Returns
    -------
    QuantLib.Index

    """
    if arg.upper() == "USDLIBOR":
        if len(args) > 0:
            return ql.USDLibor(*args)
        else:
            return ql.USDLibor()
    elif arg.upper() == "FEDFUNDS":
        if len(args) > 0:
            return ql.FedFunds(*args)
        else:
            return ql.FedFunds()
    else:
        raise ValueError("Unable to convert {} to a QuantLib index".format(arg))


def to_ql_quote_handle(arg):

    return ql.QuoteHandle(ql.SimpleQuote(arg))


def to_ql_duration(arg):

    if arg.upper() == 'MODIFIED':
        return ql.Duration.Modified
    if arg.upper() == 'SIMPLE':
        return ql.Duration.Simple
    else:
        return ql.Duration.Macaulay


def to_ql_float_index(index, tenor, yield_curve_handle=None):

    if index.upper() == "USDLIBOR":
        return ql.USDLibor(tenor, yield_curve_handle)
    elif index.upper() == "FEDFUNDS":
        return ql.FedFunds(tenor, yield_curve_handle)


def to_ql_ibor_index(index, tenor, fixing_days, currency, calendar, business_convention, end_of_month, day_counter,
                     yield_curve_handle):

    return ql.IborIndex(index, tenor, fixing_days, currency, calendar, business_convention, end_of_month, day_counter,
                        yield_curve_handle)


def to_ql_short_rate_model(arg):

    if arg.upper() == 'HULL_WHITE':
        return ql.HullWhite
    elif arg.upper() == 'BLACK_KARASINSKI':
        return ql.BlackKarasinski
    elif arg.upper() == 'G2':
        return ql.G2
