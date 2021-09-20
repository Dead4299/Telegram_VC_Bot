HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["8893915"])
    API_HASH = environ["a0940bc742c6ab70f1d3928d8de1b054"]
    SESSION_STRING = environ[
        "BQAWF87Be3AxCE-3pww8HQ18CXYiyHkThYLIUgm3Dug3AnkShmNZpck7enFkvy53Koe-s1Uu255w3YULExxu4WbCpZBvNMXAYVtl-FPRaN8_XUaGImowZJcnZIdr5IKm2pReiGO2jdcVvLXj1lVspRyoNarmxDwmJL9OQsOCJ5tyJAqLMpC_NjkdVh9G9Y7fhp3gZpOBFCw5LbeKarRMWPP5u5Dy-xoz3lqr3HH4dc6Npz-FRNNJiRZZDPl7yRoSg8Qi51PE_8amMeYWbtyWivdvX-Vb_pO72NlLi858ikfb3J1S5rlMzgEBXlWRcQnkO8PfynjcIELijxwvZu8tfTXrSeQN1gA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
