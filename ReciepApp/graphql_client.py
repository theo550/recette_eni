import requests

GRAPHQL_URL = "http://localhost:3000/graphql"

def graphql_query(query, variables=None):
    response = requests.post(
        GRAPHQL_URL,
        json={"query": query, "variables": variables or {}}
    )
    return response.json()