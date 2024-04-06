import praw

reddit = praw.Reddit(
    user_agent = "Delguard",
    client_id = "6WkJjC3repmR74-Jgg09fw",
    client_secret = "-Db2z_gzhj6cbidpzbrCJH0CWivSgw",
    username = "DelGuard",
    password = "Daksh@181")

# Define the keywords or subreddits to search for incidents
keywords = ['fire', 'water leakage', 'road collapse', 'trash pile']

# Mapping of incident types to government agencies
incident_to_agency = {
    'fire': 'Delhi Fire Department',
    'water leakage': 'Delhi Jal Board',
    'road collapse': 'Delhi Municipal Corporation',
    'trash pile': 'Delhi Municipal Corporation'
}

# Search for relevant incidents and tag government agencies
def search_and_tag():
    subreddit = reddit.subreddit('indiasocial')  # Replace with the subreddit you want to monitor
    
    for keyword in keywords:
        incidents = subreddit.search(keyword, limit=10)  # Adjust the limit as per your needs
        
        for incident in incidents:
            # Extract location information from the incident (if available)
            location = extract_location(incident)
            
            if location:
                agency = incident_to_agency[keyword]
                comment = f"Hey, {agency}! There's a {keyword} incident reported at {location}. Can you please look into it?"
                
                # Post a comment tagging the relevant government agency
                incident.reply(comment)

# Helper function to extract location information from incidents
def extract_location(incident):
    # Implement your logic to extract location information from the incident
    # This could involve searching for specific patterns or parsing the incident text
    
    return "Delhi"  # Replace with the extracted location

# Call the search_and_tag function to start monitoring and tagging incidents
search_and_tag()

