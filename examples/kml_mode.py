"""
Example: KML Mode

This mode creates a KML file that can be imported directly into Google My Maps.
"""

from pyleadfinder import leadfinder

# Your API key
API_KEY = "YOUR_API_KEY"

# Geographic bounds for Portland, OR
BOUNDS = (45.4, 45.6, -122.8, -122.5)  # (min_lat, max_lat, min_lng, max_lng)

print("Running PyLeadFinder in KML Mode...")

results = leadfinder(
    places_api_key=API_KEY,
    queries=["coffee shops"],
    output_name="coffee_shops_map",
    bounds=BOUNDS,
    radius=20,
    output_mode="kml",  # Explicitly set to KML mode
    excluded_keywords=['voodoo doughnuts'],
    scrape_emails=True
)

print(f"\nSearch complete!")
print(f"Total companies found: {results['stats']['total_companies']}")
print(f"Output files generated: {results['output_files']}")
