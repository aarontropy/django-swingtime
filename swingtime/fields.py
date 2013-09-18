from django.db import models
from dateutil import rrule

# rrule.MO = 0, etc.
weekdays = [rrule.MO, rrule.TU, rrule.WE, rrule.TH, rrule.FR, rrule.SA, rrule.SU]

class RRuleWeekdayField(models.IntegerField):

	description = "Model field to contain dateutil.rrule.weekday object"

	def to_python(self, value):
		if isinstance(value, rrule.weekday):
			return value

		return weekdays[value]

	def get_prep_value(self, value):
		return value.weekday


class RRuleWeekdayListField(models.CharField):
	'''
	Weekdays will be stored in a charfield as a comma-separated list of integers

	'''

	description = "A list of dateutil.rrule.weekday objects"

	def to_python(self,value):
		if isinstance(value, list):
			return value

		return [int(s) for s in value.split(',')]

	def get_prep_value(self, value):
		return ','.join([str(d) for d in value])

