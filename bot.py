import slack
import logging
import os 
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(os.getenv("SIGNING_SECRET"),'/slack/events',app)

client = slack.WebClient(token=os.getenc('SLACK_TOKEN'))
BOT_ID = client.api_call("auth.test")['user_id']

print("bot id", BOT_ID)
welcome_messages = {}


class weekInfo:
	def __init__(self, channel, user ):
		self.icon_emoji = ':robot_face:'
		self.user_id = user
		self.channel = channel

	def _get_info(self):
		return {
		'username': 'Mentor Bot!',
         'icon_emoji': self.icon_emoji,
         "channel": self.channel,
  		"text": "Mentor Bot Weekly Links",
		"blocks": [
			{
				"type": "header",
				"text": {
					"type": "plain_text",
					"text": "Week Breakdown",
				}
			},
			{
				"type": "section",
				"fields": [
					{
						"type": "mrkdwn",
						"text": "*Week 1 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%201%20Resources|Link>"
					},
					{
						"type": "mrkdwn",
						"text": "*Week 6 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%206%20Resources|Link>"
					}
				]
			},
			{
				"type": "section",
				"fields": [
					{
						"type": "mrkdwn",
						"text": "*Week 2 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%201%20Resources|Link>"
					},
					{
						"type": "mrkdwn",
						"text": "*Week 7 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%207%20Resources|Link>"
					}
				]
			},
			{
				"type": "section",
				"fields": [
					{
						"type": "mrkdwn",
						"text": "*Week 3 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%203%20Resources|Link>"
					},
					{
						"type": "mrkdwn",
						"text": "*Week 8 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%208%20Resources|Link>"
					}
				]
			},
			{
				"type": "section",
				"fields": [
					{
						"type": "mrkdwn",
						"text": "*Week 4 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%204%20Resources|Link>"
					},
					{
						"type": "mrkdwn",
						"text": "*Week 9 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%209%20Resources|Link>"
					}
				]
			},
			{
				"type": "section",
				"fields": [
					{
						"type": "mrkdwn",
						"text": "*Week 5 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%205%20Resources|Link>"
					},
					{
						"type": "mrkdwn",
						"text": "*Week 10 Link:*\n<https://canvas.vt.edu/courses/153792/files/folder/Week%2010%20Resources|Link>"
					}
				]
			}
		]
	}

class peer_info():
	def __init__(self, channel, user ):
		self.icon_emoji = ':robot_face:'
		self.user_id = user
		self.channel = channel

	def _get_info(self):
		return {
		'username': 'Mentor Bot!',
         'icon_emoji': self.icon_emoji,
         "channel": self.channel,
  		"text": "Mentor Bot Weekly Links",
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Peer Leader Contact Info*:"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Name:*\nKelli Carpender\n*Year:*\nSenior\n*Major:* Industrial Systems Engineering\n*Email* kellic199@vt.edu\n*Number:* "
				},
				"accessory": {
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
					"alt_text": "computer thumbnail"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Name:*\nEmily Muldowney\n*Year:*\nSenior\n*Major:*  Industrial Systems Engineering\n*Email* emilymuldowney0@vt.edu\n*Number:* "
				},
				"accessory": {
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
					"alt_text": "computer thumbnail"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Name:*\nEmily Rogers\n*Year:*\nSenior\n*Major:* Biomedical Engineering\n*Email* eprogers@vt.edu\n*Number:* "
				},
				"accessory": {
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
					"alt_text": "computer thumbnail"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Name:*\nColby Rosser\n*Year:*\nJunior\n*Major:* Industrial Systems Engineering\n*Email* colbross20@vt.edu\n*Number:*"
				},
				"accessory": {
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
					"alt_text": "computer thumbnail"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Name:*\nHaisam Saied\n*Year:*\nSenior\n*Major:* Mechanical Engineering\n*Email* haisamsaied@vt.edu\n*Number:* "
				},
				"accessory": {
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
					"alt_text": "computer thumbnail"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Name:*\nMax Sasaki\n*Year:*\nSenior\n*Major:* Civil Engineering\n*Email* msasaki26@vt.edu\n*Number:* "
				},
				"accessory": {
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
					"alt_text": "computer thumbnail"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Name:*\nAntonio Alonso\n*Year:*\nSenior\n*Major:* Computer Engineering\n*Email* antonioa19@vt.edu\n*Number:* 703-362-1145 "
				},
				"accessory": {
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
					"alt_text": "computer thumbnail"
				}
			}
		]
}
		
class mentee_info():
	def __init__(self, channel, user ):
		self.icon_emoji = ':robot_face:'
		self.user_id = user
		self.channel = channel

	def _get_info(self):
		return {
		'username': 'Mentor Bot!',
         'icon_emoji': self.icon_emoji,
         "channel": self.channel,
  		"text": "Mentor Bot Weekly Links",
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Mentee List!*"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Mentee List Link:* <https://virginiatech.sharepoint.com/:x:/r/sites/CEEDPeerMentoring-PeerMentors/Shared%20Documents/Peer%20Mentors/Fall%202022/2022%20CEED%20Peer%20Mentor%20Mentee%20Assignment%20List%20Updated.xlsx?d=w015159f4eed0407dbe1e105b96d86144&csf=1&web=1&e=sOM2lP| Link> \n "
				}
			}
		]
	}

class invite():
	def __init__(self, channel):
		self.channel = channel

	def _get_info(self):
		return {
		'username': 'Mentor Bot!',
         'icon_emoji': self.icon_emoji,
         "channel": self.channel,
  		"text": "Mentor Bot Weekly Links",
		"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Mentee List!*"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Mentee List Link:* <https://virginiatech.sharepoint.com/:x:/r/sites/CEEDPeerMentoring-PeerMentors/Shared%20Documents/Peer%20Mentors/Fall%202022/2022%20CEED%20Peer%20Mentor%20Mentee%20Assignment%20List%20Updated.xlsx?d=w015159f4eed0407dbe1e105b96d86144&csf=1&web=1&e=sOM2lP| Link> \n "
				}
			}
		]
	}


class attendance_info():
	def __init__(self, channel, user):
		self.icon_emoji = ':robot_face:'
		self.user_id = user
		self.channel = channel

	def _get_info(self):
		return {
		'username': 'Mentor Bot!',
         'icon_emoji': self.icon_emoji,
         "channel": self.channel,
  		"text": "Mentor Bot Weekly Links",
			"blocks": [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Attendance Link!:"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*<https://forms.gle/iCj6b16eZLQSiWJr9|Tuesday Night Meeting Link>*\nTuesday, 8:00-9:00pm\nVirginia Tech Campus"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://api.slack.com/img/blocks/bkb_template_images/notifications.png",
				"alt_text": "calendar thumbnail"
			}
		},
		{
			"type": "divider"
		
		}	
	]
}
	
	
class WelcomeMessage:
    START_TEXT = {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Welcome to this awesome channel! \n\n'
                '*Get started by completing the tasks!*'
            )
        }
    }

    DIVIDER = {'type': 'divider'}

    def __init__(self, channel):
        self.channel = channel
        self.icon_emoji = ':robot_face:'
        self.timestamp = ''
        self.completed = False

    def get_message(self):
        return {
            'ts': self.timestamp,
            'channel': self.channel,
            'username': 'Welcome Robot!',
            'icon_emoji': self.icon_emoji,
            'blocks': [
                self.START_TEXT,
                self.DIVIDER,
                self._get_reaction_task()
            ]
        }

    def _get_reaction_task(self):
        checkmark = ':white_check_mark:'
        if not self.completed:
            checkmark = ':white_large_square:'

        text = f'{checkmark} *React to this message!*'

        return {'type': 'section', 'text': {'type': 'mrkdwn', 'text': text}}


def send_welcome_message(channel, user):
    if channel not in welcome_messages:
        welcome_messages[channel] = {}

    if user in welcome_messages[channel]:
        return

    welcome = WelcomeMessage(channel)
    message = welcome.get_message()
    response = client.chat_postMessage(**message)
    welcome.timestamp = response['ts']

    welcome_messages[channel][user] = welcome

def send_week_message(user_id, channel):
    info = weekInfo(channel, user_id)
    message = info._get_info()
    response = client.chat_postMessage(**message)

def send_peer_message(user_id, channel):
    info = peer_info(channel, user_id)
    message = info._get_info()
    response = client.chat_postMessage(**message)


def send_mentee_message(user_id, channel):
    info = mentee_info(channel, user_id)
    message = info._get_info()
    response = client.chat_postMessage(**message)

def send_attendance_message(user_id, channel):
    info = attendance_info(channel, user_id)
    message = info._get_info()
    response = client.chat_postMessage(**message)

@slack_event_adapter.on('messages')
def message(payload):
	print(payload)
	event = payload.get('event', {})
	channel_id = event.get('channel')
	user_id = event.get('user')
	text = event.get('text')
	print("text", text)	
	if user_id != None and BOT_ID != user_id:

		if BOT_ID.lower() in text.lower() and "help" in text.lower():
			client.chat_postMessage(channel= f'@{user_id}', text="Hi! Commands include: \n1. '\ resources': Week Breakdown Links\n2. '\info': Peer Leader Contact Info\n3. '\mentees': Link for Mentee Breakdown")

@slack_event_adapter.on('team_join')
def accept(payload):
	print(payload)
	event = payload.get('event', {})
	channel_id = event.get('channel')
	user_id = event.get('user')
	client.chat_postMessage(channel= f'@{user_id}', text="Hi and Welcome!! Commands include: \n1. '\ resources': Week Breakdown Links\n2. '\info': Peer Leader Contact Info\n3. '\mentees': Link for Mentee Breakdown")



@app.route('/resources', methods=['POST'])
def resources():
	data = request.form
	user_id = data.get('user_id')
	send_week_message(user_id, f'@{user_id}')
	return Response(), 200

@app.route('/stats', methods=['POST'])
def stats():
	data = request.form
	user_id = data.get('user_id')
	channel_id = data.get('channel_id')
	print(data)
	client.chat_postMessage(channel=channel_id, text="stats")
	return Response(), 200

@app.route('/info', methods=['POST'])
def info():
	data = request.form
	user_id = data.get('user_id')
	send_peer_message(user_id, f'@{user_id}')
	return Response(), 200

@app.route('/mentees', methods=['POST'])
def mentees():
	data = request.form
	user_id = data.get('user_id')
	send_mentee_message(user_id, f'@{user_id}')
	return Response(), 200

@app.route('/attendance', methods=['POST'])
def attendance():
	data = request.form
	user_id = data.get('user_id')
	send_attendance_message(user_id, f'@{user_id}')
	return Response(), 200

if __name__ == "__main__":
	logger = logging.getLogger()

	logger.setLevel(logging.DEBUG)
	logger.addHandler(logging.StreamHandler())
	app.run(host="0.0.0.0", port=8000)
