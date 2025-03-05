# Django + Stripe API Backend

## Описание

Этот проект представляет собой бэкенд на Django с интеграцией Stripe для обработки платежей. 


<!-- GETTING STARTED -->

## Getting Started


To get a local copy up and running follow these simple example steps.



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kadissa/stripe_project
   ```
2. Open project in your IDE, create file `.env` in the root directory

3. Enter your credentials, data in `.env` (without space, without quotes)

    for example:
   ```
   STRIPE_PUBLISHABLE_KEY=51QwNOyIyM0huXj8kzmKQ3j89CN7c6ww7
   
   ```

4. Run docker-compose:

   ```docker compose up -d --build```
5. ```docker compose exec backend python manage.py migrate```
6. ```docker compose exec backend python manage.py collectstatic ```
7. ```docker compose exec backend python manage.py createsuperuser```
8. Enter in browser address bar: http://127.0.0.1/admin/
9. Fill in the required data in the admin-panel.
10. Enter in browser address bar: http://127.0.0.1/item/1




## Contact

Alex 

kadissa70@gmail.com

Project
Link: [stripe_project](https://github.com/kadissa/stripe_project)