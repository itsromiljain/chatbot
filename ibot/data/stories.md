## fallback
- utter_default

## greeting path 1
* greet
- utter_greet

## fine path 1
* fine_normal
- utter_help

## fine path 2
* fine_ask
- utter_reply

## device issue path 1
* device_issue{"device_name":"iPhone", "notify_problem":"issue"}
- utter_ofc
- utter_device_model

## device detail path 1
* device_model{"model_name":"iPhone 5"}
- utter_year
* buy_year
- utter_issue_damage

## damage path 1
* prob_device_screen{"problem_type":"screen"}
- utter_issue_fall

## damage path 2
* answer_negative
- utter_issue_stamp

## damage path 2_1
* answer_negative
- utter_issue_stamp
* answer_negative
- utter_device_charged
* alt_reply
- utter_restart
- utter_restart_outcome

## create ticket path 1
* answer_positive
- utter_damage_screen
- utter_process_ticket
- action_create_ticket

## create ticket path 2
* answer_screen_negative
- utter_damage_screen
- utter_process_ticket
- action_create_ticket

## issue resolution path 1
* answer_screen_positive
- utter_issue_resolution
- utter_glad
- utter_anything_else

## greet ticket path 1
* greet_ticket
- utter_anything_else 

## bye path 1
* bye
- utter_bye




