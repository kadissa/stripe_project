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

3. Enter your credentials in `.env` (without space, without quotes)

    for example:
   ```
   STRIPE_PUBLISHABLE_KEY=51QwNOyIyM0huXj8kzmKQ3j89CN7c6ww7
   
   ```
4. Install and run virtual environment. 
5. Install dependency, make migrations, create superuser...

   ```pip install -r requirements.txt```

   ```python manage.py makemigrations```
    
   ```python manage.py migrate```

   ```python manage.py createsuperuser```

6. Run ```python manage.py runserver```
<!-- CONTACT -->

## Contact

Alex 

kadissa70@gmail.com

Project
Link: [stripe_project](https://github.com/kadissa/stripe_project)