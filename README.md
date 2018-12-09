# Pyprice : Python price checker

Pyprice is a price checker based on Advanced Python Scheduler and PyQuery.

## Config file syntax

```yaml
# jobs/sample.yaml

alias: 'The name of the product you want to monitor price changes'
cron:
  year: 'Value following cron syntax'
  month: 'Value following cron syntax'
  week: 'Value following cron syntax'
  day_of_week: 'Value following cron syntax'
  hour: 'Value following cron syntax'
  minute: 'Value following cron syntax'
  second: 'Value following cron syntax'
  
url: https://example.com/product-page/path
priceSelector: '#PyQuery / jQuery Selector to get the price'
pbToken: 'optional/youPushBulletAPIToken'
```

