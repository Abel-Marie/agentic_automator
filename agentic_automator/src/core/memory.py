import chromadb
from chromadb.config import Settings as ChromaSettings
from agentic_automator.config.settings import settings
import json
from typing import List, Dict, Any

class Memory:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.DB_PATH)
        self.collection = self.client.get_or_create_collection(name="tools")

    def add_tool(self, tool_name: str, tool_code: str, description: str, arguments: Dict[str, Any]):
        """
        Adds a tool to the vector DB.
        """
        metadata = {
            "description": description,
            "arguments": json.dumps(arguments),
            "tool_name": tool_name
        }
        
        self.collection.add(
            documents=[description], # We embed the description for semantic search
            metadatas=[metadata],
            ids=[tool_name]
        )

    def find_tools(self, query: str, n_results: int = 3) -> List[Dict[str, Any]]:
        """
        Finds relevant tools for a given query.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        tools = []
        if results['ids']:
            for i, tool_id in enumerate(results['ids'][0]):
                tools.append({
                    "name": tool_id,
                    "description": results['metadatas'][0][i]['description'],
                    "arguments": json.loads(results['metadatas'][0][i]['arguments'])
                })
        return tools

memory = Memory()