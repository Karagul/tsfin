import numpy as np
import QuantLib as ql
from tsfin.instruments.swaprate import SwapRate
from tsfin.base.qlconverters import to_ql_calendar, to_ql_day_counter, to_ql_rate_index, to_ql_business_convention, \
    to_ql_quote_handle, to_ql_date, to_ql_ibor_index, to_ql_currency
from tsfin.constants import MATURITY_TENOR, INDEX_DAY_COUNT, CURRENCY


class SwapOption(SwapRate):

    def __init__(self, timeseries):
        super().__init__(timeseries)
        self.term_structure = ql.RelinkableYieldTermStructureHandle()
        self.index_day_count = to_ql_day_counter(self.ts_attributes[INDEX_DAY_COUNT])
        self.currency = to_ql_currency(self.ts_attributes[CURRENCY])
        self.month_end = False
        self.index = to_ql_ibor_index('{0}_Libor'.format(self.currency), self._index_tenor, self.fixing_days,
                                      self.currency, self.calendar, self.business_convention,
                                      self.month_end, self.index_day_count, self.term_structure)
        self.calendar = ql.JointCalendar(self.fixed_calendar, self.index_calendar)
        self.maturity_tenor = ql.PeriodParser.parse(self.ts_attributes[MATURITY_TENOR])
        self.fixed_leg_tenor = ql.Period(3, ql.Months)

    def rate_helper(self, date, last_available=True, *args, **kwargs):

        rate = self.quotes.get_values(index=date, last_available=last_available, fill_value=np.nan)

        if np.isnan(rate):
            return None
        rate /= 100
        return ql.SwaptionHelper(self.maturity_tenor, self._tenor, to_ql_quote_handle(rate), self.index,
                                 self.fixed_leg_tenor, self.day_counter, self.index.dayCounter(), self.term_structure)

    def set_yield_curve(self, yield_curve):

        self.term_structure.linkTo(yield_curve)