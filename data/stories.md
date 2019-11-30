## first conversation
* greet_first_time
  - utter_greet_first_time

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## opening hours
* greet
  - utter_greet
* query_knowledge_base
  - action_query_knowledge_base
* goodbye
  - utter_goodbye

## query attribute
* query_knowledge_base
  - action_query_knowledge_base

## query exchange rate
* query_exchange_rate
  - action_query_exchange_rate

## query chuck norris
* query_chuck_norris
  - action_query_chuck_norris

## query search banks
* query_search_banks
  - action_query_search_banks
<!--* inform {"latitude":"64.153960","longitude":"-21.950570"}
  - utter_thanks_for_location
  - action_query_search_banks-->

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## story thankyou
* thankyou
    - utter_noworries

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## ask how doing
* ask_how_doing
  - utter_ask_how_doing

## ask builder
* ask_builder
  - utter_ask_builder

## handle insult
* handle_insult
  - utter_handle_insult

## ask languages bot
* ask_languages_bot
  - utter_ask_languagesbot
