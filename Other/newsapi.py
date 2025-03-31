import requests

API_KEY = "70138bfd23f9409787ba1f672a14a74e"  # Replace with your API key
BASE_URL = "https://newsapi.org/v2/top-headlines"

print("Select a News Category:")
print("1. Business\n2. Entertainment\n3. General\n4. Health\n5. Science\n6. Sports\n7. Technology")

choice = int(input("Enter category number: "))

sports_query = None
match choice:
    case 1:
        category = "business"
    case 2:
        category = "entertainment"
    case 3:
        category = "general"
    case 4:
        category = "health"
    case 5:
        category = "science"
    case 6:
        category = "sports"
        print("\nSelect a Sport:")
        print("1. Football\n2. Cricket\n3. Basketball\n4. Tennis\n5. Other")
        sport_choice = int(input("Enter sport number: "))
        match sport_choice:
            case 1:
                sports_query = "football"
            case 2:
                sports_query = "cricket OR IPL OR T20 OR Ashes"
            case 3:
                sports_query = "basketball"
            case 4:
                sports_query = "tennis"
            case 5:
                sports_query = input("Enter your own sport keyword: ").strip()
            case _:
                sports_query = None
    case 7:
        category = "technology"
    case _:
        category = "general"  # Default if input is out of range

print(f"\nFetching {category.capitalize()} news...\n")

params = {
    "country": "in",  # Change to your preferred country (e.g., "in" for India)
    "category": category,  # You can change categories (e.g., "business", "sports")
    "apiKey": API_KEY
}

if sports_query:
    params["q"] = sports_query

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    articles = data.get("articles", [])
    
    for i, article in enumerate(articles[:5], 1):  # Get top 5 articles
        title = article.get("title", "No Title")
        source = article["source"].get("name", "Unknown Source")
        url = article.get("url", "No URL")
        description = article.get("description", "No Description Available")
        content = article.get("content", "Full content not available. Read more at the link below.")

        print(f"{i}. {title}")
        print(f"   Source: {source}")
        print(f"   URL: {url}")
        print(f"   Description: {description}\n")
        print(f"   Full Article: {content}\n")
        print("=" * 80)
        
else:
    print(f"Error: {response.status_code}, {response.text}")
