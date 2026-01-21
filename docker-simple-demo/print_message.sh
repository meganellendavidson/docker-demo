#!/bin/bash
MESSAGES=("Hello Docker!" "Containers are awesome" "You did it!")
RANDOM_MESSAGE=${MESSAGES[$RANDOM % ${#MESSAGES[@]}]}
figlet "$RANDOM_MESSAGE"
