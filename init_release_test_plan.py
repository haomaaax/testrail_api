from testrail import *
from pprint import *
import argparse

client = APIClient('https://inline.testrail.io/')
client.user = '__YOUR_TESTRAIL_ACCOUNT__'
client.password = '__YOUR_API_KEY__'

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--weekdate", dest="weekdate", help = "Specify week and date.")
args = parser.parse_args()

init_test_plan = {
    "name": f"Regular Release - Week {args.weekdate}", # Test plan name & sys args variable
    "entries": [
        {
            "suite_id": 1,
            "name": "Regression",    # Test run name
            "include_all": False,    # Don't include all test cases
            "assignedto_id": 37,    # Assign to userID
            "case_ids": [5712]    # Specify test case ID to be included in this test run
        },
        {
            "suite_id": 1,    # You can add multiple test runs
            "name": "Channel's Regression",
            "include_all": False,
            "assignedto_id": 28,
            "case_ids": [5713]
        }
    ]
}
new_test_plan = client.send_post('add_plan/1', init_test_plan)    # Use your project ID that you want to add your test plan to.
test_plan_url = new_test_plan.get("url")

print(test_plan_url)    # Print out test plan url to access