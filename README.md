# Installation Steps

To install the Titanic MCP server, run the following command:
```json

{
    "mcpServers":{
        "Titanic":{
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/carlosGalisteo/mcp_server_titanic.git",
                "mcp-server-titanic"
            ]
        }
    }
}