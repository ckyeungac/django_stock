from django.db import models


class Product(models.Model):
    name = models.CharField('product name', max_length=50)
    short_name = models.CharField('short name', max_length=4)
    description = models.CharField('description', max_length=255, null=True)


class Tick(models.Model):
    product = models.ForeignKey(Product)
    time = models.DateTimeField('transaction time')
    price = models.FloatField('transaction price')
    volume = models.FloatField('transaction volume')


class OHLC(models.Model):
    """
    OHLC information at each minutes
    """
    product = models.ForeignKey(Product, related_name='ohlc')
    time = models.DateTimeField('Time')
    open = models.FloatField('Open')
    high = models.FloatField('High')
    low = models.FloatField('Low')
    close = models.FloatField('Close')
    volume = models.FloatField('Volume')


class AvgStd(models.Model):
    product = models.ForeignKey(Product, related_name='avg_std')
    time = models.DateTimeField('Time')
    avg = models.FloatField('Avg Price in the day')
    std = models.FloatField('Std of Price in the day')