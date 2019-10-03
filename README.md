# docker-hello-world-text
Create an Ubuntu hello world container that sends a text message to a cell phone.

Step 1

docker build -t ub-text-1 .

Step 2

docker run -itd ub-text-1 python text.py

