from django.db import models
from dateutil import rrule

# rrule.MO = 0, etc.
weekdays = [rrule.MO, rrule.TU, rrule.WE, rrule.TH, rrule.FR, rrule.SA, rrule.SU]

class RRuleWeekdayField(models.Field):

	description = "Model field to contain dateutil.rrule.weekday object"

	def to_python(self, value):
		if isinstance(value, rrule.weekday):
			return value

		return weekdays[value]

	def get_prep_value(self, value):
		return value.weekday
