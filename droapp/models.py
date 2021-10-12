from django.db import models
from datetime import datetime, timezone, timedelta

# PC represents Periodic Cycle
class LadyPCDetail(models.Model):
    last_period_date = models.DateField()
    cycle_average = models.FloatField()
    period_average = models.IntegerField()
    # start_date = models.DateField(auto_now_add=True)
    # end_date = models.DateField(auto_now=True)
    
    @property
    def period_start_date(self):
        return self.last_period_date + timedelta(self.cycle_average)
    
    def period_end_date(self):
        return self.period_start_date + timedelta(self.period_average)
    
    def ovulation_date(self):
        return period_start_date + timedelta((cycle_average/2))
    
    def fertility_window(self):
        return self.ovulation_date - timedelta(4), 'and', self.ovulation_date + timedelta(4)
    
    def pre_ovulation_window(self):
        return self.period_end_date + timedelta(1), 'to', self.fertility_window - timedelta(1)
    
    def post_ovulation_window(self):
        return self.fertility_window + timedelta(4), 'to', self.period_start_date - timedelta(4)
    
    def __str__(self):
        return self.id