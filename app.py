from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import subprocess, os, queue, threading, logging, time

app = Flask(__name__, template_folder = './static', static_folder = './static')
logging.getLogger().setLevel(logging.INFO)
q = queue.Queue() # Create a FIFO queue
lock = threading.Lock() # Create a lock
run_with_ngrok(app) # Start ngrok when app running

@app.route('/')
def hello():
  return render_template('hello.html')

@app.route('/print', methods=['GET', 'POST'])
def print():
  if request.method == 'GET':
    return render_template("hello.html")

  info = None
  q.put(request.form['content']+'\n\n')
  app.logger.info("queue size is {} \n".format(q.qsize()))
 
  while not q.empty():
    content = q.get()  # Remove and return the first item from the queue (because I use the FIFO queue)
    lock.acquire() # Change the state to locked, a printing is starting
    try:
      if(subprocess.check_output(['exe\paperang-test.exe', content])):
        info = "已打印: "+ content
        lock.release() # The printing is done, change the state to unlocked
        app.logger.info("printed: "+ content + "\n")
    except:
      info = "Error: connect to printer failed"
      app.logger.error(info)
  return render_template('hello.html', info = info)

if __name__ == '__main__':
  app.run()