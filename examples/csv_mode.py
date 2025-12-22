"""
Example: CSV Mode

This mode exports all found leads to a CSV file.
"""

from pyleadfinder import leadfinder

# Your API key
API_KEY = "API_KEY"

# Geographic bounds for Portland, OR
BOUNDS = (45.4, 45.6, -122.8, -122.5)  # (min_lat, max_lat, min_lng, max_lng)

print("Running PyLeadFinder in CSV Mode...")

results = leadfinder(
    places_api_key=API_KEY,
    queries=["barbers"],
    output_name="portland_barbers",
    bounds=BOUNDS,
    radius=10,
    output_mode="csv"  # Explicitly set to CSV mode
)

print(f"\nSearch complete!")
print(f"Total companies found: {results['stats']['total_companies']}")
print(f"Output files generated: {results['output_files']}")
