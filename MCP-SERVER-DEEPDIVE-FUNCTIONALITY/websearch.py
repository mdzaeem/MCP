from mcp.server.mcpserver import MCPServer
from openai import OpenAI

YOUR_API_KEY = 'YOUR_API_Here'

mcp = MCPServer("Web Search")

@mcp.tool()
def perform_websearch(query: str) -> str:
    """
    Performs a web search for a query
    Args:
        query: the query to web search.
    """

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant that searches the web and responds to questions"
            ),
        },
        {   
            "role": "user",
            "content": (
                query
            ),
        },
    ]

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

    # chat completion without streaming
    response = client.chat.completions.create(
        model="sonar",
        messages=messages,
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    mcp.run()