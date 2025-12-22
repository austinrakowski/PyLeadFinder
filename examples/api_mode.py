"""
Example: API Mode (Default)

This mode returns data directly as a dictionary without creating any files.
It is the default mode and is ideal for integration into other applications or scripts.
"""

from pyleadfinder import leadfinder
import json

# Your API key
API_KEY = "YOUR_API_KEY"

# Geographic bounds for Portland, OR
BOUNDS = (45.4, 45.6, -122.8, -122.5)  # (min_lat, max_lat, min_lng, max_lng)

print("Running PyLeadFinder in API Mode (Default)...")

results = leadfinder(
    places_api_key=API_KEY,
    queries=["gyms"],
    bounds=BOUNDS,
    radius=5,
    # output_mode="api",  # This is now the default, so we can omit it
    scrape_emails=False
)

# The results are a dictionary containing companies, stats, and map_data
print(f"\nFound {results['stats']['total_companies']} companies")

# Example of processing the data
if results['companies']:
    company = results['companies'][0]
    print(f"\nSample Company Data:")
    print(json.dumps(company, indent=2))

print("\nStats:")
print(json.dumps(results['stats'], indent=2))
