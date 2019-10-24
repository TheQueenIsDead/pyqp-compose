#!/usr/bin/env bash



send_message() {
    message=$1
    python ./send.py "\"${message}\""
    sleep 1 # Just to pause between execution
}

send_message "Hiya, this is exciting!"
send_message "Hello world!"
send_message "Third message now...cool"
send_message "Tired, hopping off to bed"
send_message "See you soon!"
