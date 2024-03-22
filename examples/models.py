from django.db import models


from django.utils.translation import gettext_lazy as _
from django.core.validators import BaseValidator

from datetime import datetime

# Create your models here.

class TradeStatus(models.TextChoices):
    ACTIVE = "ACTV", _("active")
    CONFIRMED = "CONF", _("confirmed")
    CANCELLED = "CANC", _("cancelled")
    PENDING = "PEND", _("pending")

    def from_label(label):
        # field is the uppercase of the label
        return TradeStatus._member_map_[label.upper()]


class TradeSide(models.TextChoices):
    BUY = "B", _("buy")
    SELL = "S", _("sell")

    def from_label(label):
        # field is the uppercase of the label
        return TradeSide._member_map_[label.upper()]


# Positive value validator, call clean_fields to activate
class MinValueValidator(BaseValidator):
    message = _('Ensure this value is greater than or equal to %(limit_value)s.')
    code = 'min_value'

    def compare(self, a, b):
        return a < b  # super simple.

""" 
    Actual models
"""

class Bond(models.Model):
    name = models.CharField(max_length=16, unique=True)                                    # bond string identifier
    market_bid = models.FloatField(validators=[MinValueValidator(0)], default=0, blank=True)    # last-recorded market bid

class Broker(models.Model):
    name = models.CharField(max_length=16, unique=True)       # broker identifier

class Currency(models.Model):
    name = models.CharField(max_length=3, unique=True)

# local transaction table
# TODO: setup foreign keys models.ForeignKey(classname, on_delete=models.CASCADE)
class Transaction(models.Model):
    #id = models.AutoField()                             # id primary key, not necessary as added by default

    trade_status = models.CharField(                    # trade status
        max_length=4,
        choices=TradeStatus,
        default=TradeStatus.PENDING,
    )

    trade_side = models.CharField(                      # trade side
        max_length=1,
        choices=TradeSide
    )
    
    bond = models.ForeignKey(Bond, null=True, blank=True, on_delete=models.CASCADE)        # the bond that was exchanged
    broker = models.ForeignKey(Broker, null=True, blank=True, on_delete=models.CASCADE)    # the broker to which the exchange occured
    user = models.CharField(max_length=32) #models.ForeignKey(User, on_delete=models.CASCADE)        # user responsible of the transaction

    trade_datetime = models.DateTimeField(default=datetime.now())    # date of the trade
    modif_datetime = models.DateTimeField(auto_now=True)        # last modification date of the trade
    settlement_datetime = models.DateTimeField(default=None, null=True, blank=True)    # settlement date of the trade

    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE) # currency

    market_price = models.FloatField(                   # market price at the moment of the transaction
            validators=[MinValueValidator(0)]
    )
    quantity = models.FloatField(                  # quantity or amount issued in terms of money
            validators=[MinValueValidator(0)]
    )

    security = models.TextField(default='', blank=True)           # description of the overall transaction, given by Bloomberg

    comments = models.TextField(default='', blank=True)           # eventual comments



    
# global transaction
"""
class ConfirmedTransaction(models.Model):
    remote_id = models.CharField(max_length=32, primary_key=True)                                    # Bloomberg remotely assigned id 
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)                        # transaction of reference
    
    # set that there exist only one remote_id per transaction occured
    class Meta:         
        unique_together = (("remote_id", "transaction"),)
"""  
