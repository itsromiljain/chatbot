## greeting path1
* greet
- utter_greet
* fine_normal
- utter_help

## greeting path2
* greet
- utter_greet
* fine_ask
- utter_reply

## goodbye
* bye
- utter_bye

## assisting
* ask_help
- utter_ofc

## fallback
- utter_default

## phone path 1
* issue_phone{"device_name":"iPhone"}{"notify_problem":"issue"}
- utter_model_phone
* model_phone{"model_name":"iPhone 5"}
- utter_year
* buy_year
- utter_issue_damage
* prob_phone_screen{"problem_type":"screen"}
- utter_issue_fall
* answer_negative
- utter_issue_stamp
* answer_negative
- utter_device_charged
* answer_positive
- utter_alts2
* alt_reply
- utter_ask
* answer_negative
- utter_alts3
* alt_reply
- utter_ask
* answer_negative
- utter_damage_screen
- utter_process_ticket
- action_create_ticket
* greet_ticket
- utter_anything_else

## path11
* issue_phone{"device_name":"iPhone"}{"notify_problem":"issue"}
- utter_model_phone
