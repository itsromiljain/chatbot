## greet with name happy path
* greet{"Person": "manoj"}
- utter_greetwithname
* mood_great
- utter_goodtohear
* restaurant_search
- utter_typeofcuisine
* restaurant_search{"cuisine": "chinese"}
- utter_whichlocation
* restaurant_search{"location": "north"}
- utter_api
- utter_restaurants
* thankyou
- utter_thankyou
- action_restart

## happy path with cuisine
* greet
- utter_greet
* mood_great
- utter_goodtohear
* restaurant_search{"cuisine": "chinese"}
- utter_whichlocation
* restaurant_search{"location": "north"}
- utter_api
- utter_restaurants
* thankyou
- utter_thankyou

## happy path with location
* greet
- utter_greet
* mood_great
- utter_goodtohear
* restaurant_search{"location": "west"}
- utter_typeofcuisine
* restaurant_search{"cuisine": "mexican"}
- utter_api
- utter_restaurants
* thankyou
- utter_thankyou

## greet with restaurant search
* greet
- utter_greet
* restaurant_search
- utter_typeofcuisine
* restaurant_search{"cuisine": "indian"}
- utter_whichlocation
* restaurant_search{"location": "29432"}
- utter_api
- utter_restaurants
* thankyou
- utter_thankyou

## greet bad mood restaurant search
* greet
- utter_greet
* mood_unhappy
- utter_cheer_up
* restaurant_search
- utter_typeofcuisine
* restaurant_search{"cuisine": "indian"}
- utter_whichlocation
* restaurant_search{"location": "west"}
- utter_api
- utter_restaurants
* thankyou
- utter_thankyou

## happy path with location cuisine
* greet
- utter_greet
* mood_great
- utter_goodtohear
* restaurant_search{"cuisine": "indian","location": "north"}
- utter_api
- utter_restaurants
* thankyou
- utter_thankyou

## greet bad mood restaurant_search with cuisine
* greet
- utter_greet
* mood_unhappy
- utter_cheer_up
* restaurant_search{"cuisine":"indian"}
- utter_whichlocation
* restaurant_search{"location":"west"}
- utter_api
- utter_restaurants
* thankyou
- utter_thankyou




