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
Override according to attribute values in your database.
TODO: Implement a good way to override these constants (e.g.: with a config file).
"""

'''
Special names.
'''
QUOTES = 'PRICE'  # Name (in the database) of the component representing the quotes of an instrument.

'''
Database attribute keys
'''
TYPE = 'TYPE'
BOND_TYPE = 'SUBTYPE'
QUOTE_TYPE = 'QUOTE_TYPE'
CURRENCY = 'CURRENCY'
YIELD_QUOTE_COMPOUNDING = 'YIELD_QUOTE_COMPOUNDING'
COMPOUNDING = 'COMPOUNDING'
YIELD_QUOTE_FREQUENCY = 'YIELD_QUOTE_FREQUENCY'
FREQUENCY = 'FREQUENCY'
ISSUE_DATE = 'ISSUE_DATE'
FIRST_ACCRUAL_DATE = 'FIRST_ACCRUAL_DATE'
MATURITY_DATE = 'MATURITY'
TENOR_PERIOD = 'TENOR'
COUPON_FREQUENCY = 'FREQUENCY'
CALENDAR = 'CALENDAR'
BUSINESS_CONVENTION = 'BUSINESS_CONVENTION'
DATE_GENERATION = 'DATE_GENERATION'
SETTLEMENT_DAYS = 'SETTLEMENT_DAYS'
FACE_AMOUNT = 'FACE_AMOUNT'
COUPONS = 'COUPON'
DAY_COUNTER = 'DAY_COUNT'
REDEMPTION = 'REDEMPTION'
INDEX = 'INDEX'
INDEX_TENOR = 'INDEX_TENOR'
INDEX_TIME_SERIES = 'INTEREST_TIME_SERIES'
SPREAD = 'SPREAD'
BASE_CURRENCY = 'BASE_CURRENCY'
COUNTER_CURRENCY = 'COUNTER_CURRENCY'
BASE_RATE_DAY_COUNTER = 'BASE_RATE_DAY_COUNTER'
BASE_RATE_COMPOUNDING = 'BASE_RATE_COMPOUNDING'
BASE_RATE_FREQUENCY = 'BASE_RATE_FREQUENCY'
COUNTER_RATE_DAY_COUNTER = 'COUNTER_RATE_DAY_COUNTER'
COUNTER_RATE_COMPOUNDING = 'COUNTER_RATE_COMPOUNDING'
COUNTER_RATE_FREQUENCY = 'COUNTER_RATE_FREQUENCY'
PAYMENT_LAG = 'PAYMENT_LAG'
FIXING_DAYS = 'FIXING_DAYS'
EXERCISE_TYPE = 'EXERCISE_TYPE'
OPTION_TYPE = 'OPTION_TYPE'
STRIKE_PRICE = 'STRIKE_PRICE'
UNDERLYING_INSTRUMENT = 'UNDERLYING_INSTRUMENT'
OPTION_CONTRACT_SIZE = 'OPTION_CONTRACT_SIZE'
RECOVERY_RATE = 'RECOVERY_RATE'
SPREAD_TAG = 'SPREAD_TAG'
BASE_SPREAD_TAG = 'BASE_SPREAD_TAG'

'''
Database attribute values
'''
BOND = 'BOND'
FIXEDRATE = 'FIXEDRATE'
CALLABLEFIXEDRATE = 'CALLABLEFIXEDRATE'
FLOATINGRATE = 'FLOATINGRATE'
DISCOUNT = 'DISCOUNT'
CLEAN_PRICE = 'CLEAN_PRICE'
DIRTY_PRICE = 'DIRTY_PRICE'
YIELD = 'YIELD'
DEPOSIT_RATE = 'DEPOSIT_RATE'
DEPOSIT_RATE_FUTURE = 'DEPOSIT_RATE_FUTURE'
CURRENCY_FUTURE = 'CURRENCY_FUTURE'
SWAP_RATE = 'SWAP_RATE'
OIS_RATE = 'OIS'
EQUITY_OPTION = 'EQUITY_OPTION'
RATE_INDEX = 'RATE_INDEX'
FUND = 'FUND'
EQUITY = 'EQUITY'
CDS = 'CDS'
ZERO_RATE = 'ZERO_RATE'

'''
Configuration for yield curve classes
'''
# Names of attributes representing issue dates of securities in increasing order of precedence.
ISSUE_DATE_ATTRIBUTES = ['EFFECTIVE_PRECEDENCE_ISSUE', 'ISSUE']
