import os
import logging
import logging.config
import json
import argparse

#' initiate the logging
def start_logging(config = None):
  if logging.root:
    del logging.root.handlers[:]

  if config is None:
    config = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_config.json")
  assert config.endswith("json"), "Please use json file format for configurations"
  
  with open(config, 'r') as f:
    try:
      d = json.load(f)
      logging.config.dictConfig(d)
    except:
      logging.error("{config} could not be loaded, please use json file format for configurations".format(**locals()))

#' log the arguments
def print_cmd_args(args = None):
  assert args is not None, "Missing object of command line arguments"
  
  arg_print = "Command line args:\n"
  myargs = ["{}: {}".format(a, getattr(args, a)) for a in vars(args) if a != "log"]
  
  if len(myargs) > 0:
    arg_print += "\n".join(myargs)
    logging.info(arg_print)
  

#' process the arguments
def process_args(parser = None):
  assert parser is not None, "Input parser is missing"
  assert isinstance(parser, argparse.ArgumentParser), "Input parser must be an argparse ArgumentParser object"

  description = parser.description
  args = parser.parse_args()
  
  start_logging(args.log)
  logging.info(description)
  print_cmd_args(args)

  return args

#' sends notification email
def send_notification(email, subj = 'Notification', msg = ''):
  import smtplib
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText
  
  #creates the sender, recipient, subject, and message fields
  sender = 'automatique.sender@gmail.com'
  receivers = email
  message = MIMEMultipart()
  message['From'] = sender
  message['To'] = receivers
  message['Subject'] = subj
  message.attach(MIMEText(msg, 'plain'))
  
  try:
    #log into the gmail server
    password = 'autoGMAIL'
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
      server.ehlo()
      server.starttls()
      server.login(sender, password)
      server.sendmail(sender, [receivers], message.as_string()) #sends the email
    logging.info('Email sent successfully')
  except:
    logging.info('Error: email failed')
