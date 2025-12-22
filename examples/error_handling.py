"""
Example: Error Handling with PyLeadFinder
"""

from pyleadfinder import (
    leadfinder,
    OperationTimeoutError,
    InvalidAPIKeyError,
    QuotaExceededError,
    RateLimitError,
    NetworkError,
    PlacesAPIError,
    InvalidBoundsError,
    InvalidOutputModeError
)

# Example 1: Handling timeout errors
print("=" * 70)
print("Example 1: Timeout Handling")
print("=" * 70)

try:
    results = leadfinder(
        places_api_key="YOUR_API_KEY_HERE",
        queries=["restaurants"],
        bounds=(45.4, 45.6, -122.8, -122.5),
        output_mode="api",
        timeout=3  # short timeout for demonstration
    )
    print(f"Found {results['stats']['total_companies']} companies")
except OperationTimeoutError as e:
    print(f"Operation timed out: {e}")


# Example 2: Handling API key errors
print("\n" + "=" * 70)
print("Example 2: API Key Error Handling")
print("=" * 70)

try:
    results = leadfinder(
        places_api_key="INVALID_KEY",
        queries=["gyms"],
        bounds=(45.4, 45.6, -122.8, -122.5),
        output_mode="api"
    )
except InvalidAPIKeyError as e:
    print(f"Invalid API key: {e}")
    print(f"Status code: {e.status_code}")

# Example 3: Handling quota exceeded
print("\n" + "=" * 70)
print("Example 3: Quota Exceeded Handling")
print("=" * 70)

try:
    results = leadfinder(
        places_api_key="YOUR_API_KEY_HERE",
        queries=["coffee shops"],
        bounds=(45.4, 45.6, -122.8, -122.5),
        output_mode="api"
    )
except QuotaExceededError as e:
    print(f"API quota exceeded: {e}")
    print(f"Response data: {e.response_data}")

# Example 4: Handling network errors
print("\n" + "=" * 70)
print("Example 4: Network Error Handling")
print("=" * 70)

try:
    results = leadfinder(
        places_api_key="YOUR_API_KEY_HERE",
        queries=["bars"],
        bounds=(45.4, 45.6, -122.8, -122.5),
        output_mode="api"
    )
except NetworkError as e:
    print(f"Network error: {e}")

# Example 5: Handling validation errors
print("\n" + "=" * 70)
print("Example 5: Validation Error Handling")
print("=" * 70)

try:
    # Invalid bounds (only 3 values instead of 4)
    results = leadfinder(
        places_api_key="YOUR_API_KEY_HERE",
        queries=["hotels"],
        bounds=(45.4, 45.6, -122.8),  # Missing max_lng
        output_mode="api"
    )
except InvalidBoundsError as e:
    print(f"Invalid bounds: {e}")

try:
    # Invalid output mode
    results = leadfinder(
        places_api_key="YOUR_API_KEY_HERE",
        queries=["hotels"],
        bounds=(45.4, 45.6, -122.8, -122.5),
        output_mode="invalid_mode"
    )
except InvalidOutputModeError as e:
    print(f"Invalid output mode: {e}")

# Example 6: Catch-all error handling
print("\n" + "=" * 70)
print("Example 6: Comprehensive Error Handling")
print("=" * 70)

try:
    results = leadfinder(
        places_api_key="YOUR_API_KEY_HERE",
        queries=["restaurants"],
        bounds=(45.4, 45.6, -122.8, -122.5),
        output_mode="api",
        timeout=60
    )

    # Process results
    print(f"Success! Found {results['stats']['total_companies']} companies")

    for company in results['companies'][:5]:
        print(f"  - {company['name']}")
        if company['emails']:
            print(f"    Emails: {', '.join(company['emails'])}")

except OperationTimeoutError as e:
    print(f"Timeout: {e}")

except InvalidAPIKeyError as e:
    print(f"API Key Error: {e}")

except QuotaExceededError as e:
    print(f"Quota Exceeded: {e}")

except RateLimitError as e:
    print(f"Rate Limit: {e}")

except NetworkError as e:
    print(f"Network Error: {e}")

except (InvalidBoundsError, InvalidOutputModeError) as e:
    print(f"Validation Error: {e}")

except PlacesAPIError as e:
    print(f"Places API Error: {e}")
    print(f"   Status code: {e.status_code}")

except Exception as e:
    print(f"Unexpected error: {e}")

print("\n" + "=" * 70)
print("Error Handling Complete")
print("=" * 70)
