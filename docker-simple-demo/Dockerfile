# start with latest ubuntu image
FROM ubuntu:latest
# update ubuntu and install figlet
RUN apt-get update && apt-get install -y figlet
# copy the script into the container
COPY ./print_message.sh /app/print_message.sh
# make the script executable
RUN chmod +x /app/print_message.sh
# set the script as the container's default command
CMD ["/app/print_message.sh"]