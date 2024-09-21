# shop-feed-servers

This is a study project into microservices architecture

Plan (subject to change)
```
shop-feed services
  authentication - ? | sql
  user - spring | mysql
    contains follows
  shop - fastapi | pgsql
    contains products
  transaction - asp.net | sql
  cart - redis

apache kafka for event streaming
```
