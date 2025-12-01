"""
Example: How to call the advanceautoparts-scraper actor using Apify API Client

For full documentation of the Apify Client for Python, see: https://docs.apify.com/api/client/python
For full documentation of the actor, see: https://apify.com/lexis-solutions/advanceautoparts-scraper

Note: This example uses the Apify API Client (apify-client) to call actors from external code.
If you want to create Actors, use the Apify SDK (apify) instead:
https://docs.apify.com/sdk/python/docs/overview/introduction
"""

import os
from apify_client import ApifyClient


def run_actor():
    """Run the advanceautoparts-scraper actor and retrieve results."""
    # Initialize the ApifyClient with your API token
    # Get your API token from https://console.apify.com/account/integrations
    client = ApifyClient(token=os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN"))

    # Start the actor run and wait for it to finish
    # The .call() method starts the actor and waits for completion automatically
    actor_id = "lexis-solutions/advanceautoparts-scraper"
    print(f"Starting actor: {actor_id}")

    run = client.actor(actor_id).call(
        run_input={
            "startUrls": [{"url":"https://shop.advanceautoparts.com/c2/distributors/81732?filterValue=nVariant_categoryPath%3AP800%7CUser%20Navigation%3ED20419%7CPerformance%20Distributors%3E3020%7CPerformance%20Distributor&categoryGroupId=81732&categorySlug=distributors"}],
            "maxPages": 1,
        }
    )

    # Get the dataset ID from the completed run
    dataset_id = run["defaultDatasetId"]
    print(f"Actor run completed! Dataset ID: {dataset_id}")

    # Get the results from the dataset
    dataset_items = client.dataset(dataset_id).list_items()
    items = dataset_items.items
    print(f"Retrieved {len(items)} items from the dataset.")
    print("Results:", items)
    return items


if __name__ == "__main__":
    run_actor()
