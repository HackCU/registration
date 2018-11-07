# HACKATHON PERSONALIZATION
import os

from django.utils import timezone

HACKATHON_NAME = 'Phase'
# What's the name for the application
HACKATHON_APPLICATION_NAME = 'Phase registration'
# Hackathon timezone
TIME_ZONE = 'MST'
# This description will be used on the html and sharing meta tags
HACKATHON_DESCRIPTION = 'Apply now! HackCU is a student organization ' \
                         'at the University of Colorado at Boulder who brings together ' \
                         'people for our annual technology and design events, HackCU and Local Hack Day. ' \
                         'We are the largest hackathon in the Rocky Mountain Region, and ' \
                         'our mission is to foster learning, designing, ' \
                         'and building in order to turn student\'s ideas into a reality!'
# Domain where application is deployed, can be set by env variable
HACKATHON_DOMAIN = os.environ.get('DOMAIN', 'localhost:8000')
# Hackathon contact email: where should all hackers contact you. It will also be used as a sender for all emails
HACKATHON_CONTACT_EMAIL = 'contact@hackcu.org'
# Hackathon logo url, will be used on all emails
HACKATHON_LOGO_URL = 'https://phase.hackcu.org/assets/images/smithchart.png'

HACKATHON_OG_IMAGE = 'https://phase.hackcu.org/assets/images/ogimage870x450.png'
# (OPTIONAL) Track visits on your website
HACKATHON_GOOGLE_ANALYTICS = 'UA-111579742-1'
# (OPTIONAL) Hackathon twitter user
HACKATHON_TWITTER_ACCOUNT = 'hackcu'
# (OPTIONAL) Hackathon Facebook page
HACKATHON_FACEBOOK_PAGE = 'hackcu'
# (OPTIONAL) Github Repo for this project (so meta)
HACKATHON_GITHUB_REPO = 'https://github.com/hackcu/registration/'

# (OPTIONAL) Applications deadline
HACKATHON_APP_DEADLINE = timezone.datetime(2018, 11, 9, 23, 59, tzinfo=timezone.pytz.timezone(TIME_ZONE))
# (OPTIONAL) When to arrive at the hackathon
HACKATHON_ARRIVE = 'Registration opens at 7:00 AM and closes at 8:00 AM on Saturday November 10th, ' \
                   'the opening ceremony will be at 8:00 AM.'

# (OPTIONAL) When to arrive at the hackathon
HACKATHON_LEAVE = 'Closing ceremony will be held on Sunday November 11th from 12:00 AM to 1:00 AM. ' \
                  'However the projects demo fair will be held in the night from 11:30 PM to midnight.'
# (OPTIONAL) Hackathon live page
HACKATHON_LIVE_PAGE = 'https://live.hackcu.org'

# (OPTIONAL) Regex to automatically match organizers emails and set them as organizers when signing up
REGEX_HACKATHON_ORGANIZER_EMAIL = '^.*@hackcu\.org$'
# (OPTIONAL) Send 500 errors to email while on production mode
HACKATHON_DEV_EMAILS = ['devs@hackcu.org', ]

# Reimbursement configuration
REIMBURSEMENT_ENABLED = False
# CURRENCY = '$'
# REIMBURSEMENT_EXPIRY_DAYS = 5
# REIMBURSEMENT_REQUIREMENTS = 'You have to submit a project and demo it during the event in order to get reimbursed'
# REIMBURSEMENT_DEADLINE = timezone.datetime(2018, 1, 28, 0, 1, tzinfo=timezone.pytz.timezone(TIME_ZONE))

# (OPTIONAL) Max team members. Defaults to 4
TEAMS_ENABLED = False
# HACKATHON_MAX_TEAMMATES = 4

# (OPTIONAL) Code of conduct link
CODE_CONDUCT_LINK = "https://pages.hackcu.org/code_conduct/"

# (OPTIONAL) Slack credentials
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'test'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}

# (OPTIONAL) Logged in cookie
# This allows to store an extra cookie in the browser to be shared with other application on the same domain
LOGGED_IN_COOKIE_DOMAIN = '.hackcu.org'
LOGGED_IN_COOKIE_KEY = 'hackcu_logged_in'

# Hardware configuration
HARDWARE_ENABLED = False
#Hardware request time length (in minutes)
HARDWARE_REQUEST_TIME = 15
