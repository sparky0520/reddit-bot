import praw
import tweepy

# Reddit app credentials
reddit_client_id = "6WkJjC3repmR74-Jgg09fw"
reddit_client_secret = "-Db2z_gzhj6cbidpzbrCJH0CWivSgw"
reddit_username = "sparky_xelite"
reddit_password = "Sparky@2005"

# Twitter app credentials (API keys and tokens)
twitter_consumer_key = "mwVc9zQGm4RVYXe2aqHVZ6iyT"
twitter_consumer_secret = "gpDGqMZvPfO9u6qnlqgTDtHXVXv6qntvGNdSsS8ZqQmNEjm7gZ"
twitter_access_token = "1324319741998104576-07IGlcSaDaWMIfqRhrSQzJMkU9ci9G"
twitter_access_token_secret = "k6B5zc1MHAg60rHQbhx4yqF30IA0j5cGUOuMmDSkaIDN1"

# Define keywords for incident classification
fire_keywords = ["fire breaks out",
                 "fire tender",
                 "control fire",
                 "gutted in fire",
                 "fire broke out",
                 "fire call",
                 "fire incident",
                 "engulfed in a fire",
                 "engulfed in fire",
                 "forest fire"]
water_leakage_keywords = ["water leakage",
                          "water pipeline leakage",
                          "water pipe leakage",
                          "leakage in water pipe"]
road_damaged_keywords = [
    "road damaged",
    "roads damaged",
    "damaged road",
    "damaged roads",
    "pothole"
]
building_collapse_keywords = [
    "building collapse"
]
trash_pile_keywords = [
    "trash is piling up",
    "trash piling up",
    "garbage is piling up",
    "garbage piling up",
    "waste is piling up",
    "waste piling up"
]

# Define locations within Delhi
location_keywords = [
    "new delhi",
    "central delhi",
    "east delhi",
    "north delhi",
    "north east delhi",
    "north west delhi",
    "south delhi",
    "south east delhi",
    "south west delhi",
    "west delhi",
    "rajouri garden",
    "punjabi bagh",
    "janakpuri",
    "tilak nagar",
    "patel nagar",
    "dwarka",
    "palam",
    "mandi house",
    "moolchand",
    "central secretariat",
    "vasant vihar",
    "najafgarh",
    "dabri",
    "lajpat nagar",
    "defence colony",
    "sarita vihar",
    "kalkaji",
    "govindpuri",
    "hauz khas",
    "saket",
    "greater kailash",
    "vasant kunj",
    "defence colony",
    "rohini",
    "pitampura",
    "lok kalyan marg",
    "shalimar bagh",
    "ashok vihar",
    "wazirpur",
    "yamuna vihar",
    "bikaji kama place",
    "nehru place",
    "netaji subash place",
    "jhilmil",
    "karkarduma",
    "dilshad garden",
    "shahdara",
    "nand nagri",
    "seelampur",
    "civil lines",
    "kashmere gate",
    "okhla",
    "model town",
    "tis hazari",
    "pitampura",
    "mangolpuri",
    "kanjhawala",
    "india gate",
    "red fort",
    "qutub minar",
    "lotus temple",
    "pragati maidan",
    "narela",
    "race course",
    "malviya nagar",
    "sarojni nagar",
    "vinobapuri",
    "samaypur badli",
    "shalimar bagh",
    "wazirabad",
    "india gate",
    "rashtrapati bhavan",
    "parliament house",
    "diplomatic enclave",
    "khan market",
    "preet vihar",
    "mayur vihar",
    "shahdara",
    "gandhi nagar",
    "krishna nagar",
    "connaught place",
    "chandni chowk",
    "daryaganj",
    "paharganj",
    "karol bagh",
    "ring road",
    "mahatma gandhi road",
    "outer ring road",
    "inner ring road",
    "nh44",
    "nh48",
    "nh9",
    "delhi-gurgaon expressway",
    "delhi-noida direct flyway",
    "barapullah elevated road",
    "akshardham flyover",
    "mehrauli-gurgaon road",
    "delhi-meerut expressway",
    "noida-greater noida expressway",
    "chhatarpur road",
    "mathura road",
    "aurobindo marg",
    "bhairon marg",
    "dr. zakir hussain marg",
    "nelson mandela marg",
    "bahadur shah zafar marg",
    "gt karnal road"
]

# Initialize Reddit and Twitter clients
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent="Delhi Incident Reporter Bot")

# Authenticate Twitter
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
twitter_api = tweepy.API(auth)

# Subreddit stream for monitoring new posts
subreddit = reddit.subreddit("delhi")
for submission in subreddit.stream.submissions():

    # Skip posts by yourself or irrelevant subreddits
    if submission.author == reddit_username or submission.subreddit != "delhi":
        continue

    # Text preprocessing for classification
    text = submission.title + " " + submission.selftext.lower()

    # Classify incident type
    is_fire = any(word in text for word in fire_keywords)
    is_water_leakage = any(word in text for word in water_leakage_keywords)
    is_road_damaged = any(word in text for word in road_damaged_keywords)
    is_building_collapse = any(word in text for word in building_collapse_keywords)
    is_trash_pile = any(word in text for word in trash_pile_keywords)

    # Extract location details
    location = None
    for word in location_keywords:
        if word in text:
            location = word
            break

    if is_fire:
        incident_type = "Fire"
        # Craft tweet message
        tweet_text = f"{incident_type} reported in {location}. #DelhiFireService @DelhiFire"
    elif is_water_leakage:
        incident_type = "Water Leakage"
        # Craft tweet message
        tweet_text = f"{incident_type} reported in {location}. #Delhi जल Board @DelhiJalBoard"
    elif is_road_damaged:
        incident_type = "Road Damaged"
        # Craft tweet message
        tweet_text = f"{incident_type} reported in {location}. @MCD_Delhi @DelhiPwd #DelhiTrafficPolice"
    elif is_building_collapse:
        incident_type = "Building Collapse"
        # Craft tweet message
        tweet_text = f"{incident_type} reported in {location}. #DelhiFireService @DelhiFire"
    elif is_trash_pile:
        incident_type = "Trash Pile"
        # Craft tweet message
        tweet_text = f"{incident_type} reported in {location}. @MCD_Delhi  #SwachhDelhi"
    else:
        # Not a relevant incident, skip to next post
        continue

    # Post the tweet
    twitter_api.update_status(status=tweet_text)

    print(f"Tweeted: {tweet_text}")
