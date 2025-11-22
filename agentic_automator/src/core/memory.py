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