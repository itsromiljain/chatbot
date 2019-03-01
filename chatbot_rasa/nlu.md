## intent:greet
- hey, I am [manoj](Person)
- hello I am [gautham](Person)
- hi This is [Himansu](Person)
- good morning
- good evening
- good afternoon
- hey there This is [prachi](Person) here
- hi there
- hii

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch 
- I am searching for a dinner spot
- food [near me](location)
- [Japanese](cuisine) restaurants [near me](location:here)
- restaurants [near me](location)
- place [near me](location) to eat
- [russian](cuisine) near me
- [italian](cuisine) restaurants near me
- restaurants in the [midtown](location)
- i'm looking for a [chines](cuisine:chinese) restaurant in the [north](location) of town
- show me [chinese](cuisine) restaurants
- show me a [mexican](cuisine) place in this area
- i am looking for an [indian](cuisine) spot
- i am looking for an [Desi](cuisine:indian) restaurants
- want to eat [spicy](cuisine:indian) food
- I would like a [punjabi](cuisine:indian) food
- search for restaurants in the [center](location)
- anywhere in the [west](location)
- anywhere near [18328](zipcode)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [29432](zipcode)
- restaurants [here](location)
- looking for finest food [here](location)

## synonym:center
- central
- midtown
- middle

## regex:zipcode
- [0-9]{5}

## regex:greet
- hey[\s]*.*
- hi+[\s]*.*

## regex:restaurant_search
- [a-zA-Z0-9\s]*restaurants 
- restaurants[a-zA-Z0-9\s]*
- [a-zA-Z0-9\s]*food
- food[a-zA-Z0-9\s]*

## intent:thankyou
- thanks!
- thank you
- thx
- thanks very much
- thanks
- thankyou very much
- thanks a lot
- thanks. Have a nice day
- thanks. have a good one.
- have a good one
- okay Thanks

## intent:mood_great
- I am doing great
- I am absolutely alright
- I am fine
- I am happy. How about you
- fine
- alright
- good
- going good
- doing good
- happy
- superb
- All good. How are you?
- great
- doing great
- I am good
- absolutely fine

## regex:mood_great
- doing[\s]*(good|great|awesome)

## intent:mood_unhappy
- I am not doing good
- I am doing bad
- I am unhappy
- I am so sad
- I am not happy
- I am sick
- bad mood
- frustrating
- going mad

## intent:mood_deny
- No it didn't help
- I am not satisfied
- not okay

## intent:api
- jira
- JIRA
- create jira

