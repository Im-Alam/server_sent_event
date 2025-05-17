import json
import asyncio
from typing import Dict, Any
import random

random_number_in_range = lambda min, max: random.randint(min, max)
# Sample validation tasks for demonstration
validation_tasks = [
    {
        "layer": 1,
        "task_name": "Document Parsing",
        "status": "processing",
        "message": "Starting document analysis..."
    },
    {
        "layer": 1,
        "task_name": "Document Parsing",
        "status": "finished",
        "message": "Document parsed successfully"
    },
    {
        "layer": 2,
        "task_name": "Content Validation",
        "status": "processing",
        "message": "Checking content integrity..."
    },
    {
        "layer": 2,
        "task_name": "Content Validation",
        "sub_task_name": "Article1",
        "status": "processing",
        "message": "Validating consistency..."
    },
    {
        "layer": 2,
        "task_name": "Content Validation",
        "sub_task_name": "Article1",
        "status": "pass",
        "message": "Validation passed sucessfully"
    },
    {
        "layer": 3,
        "task_name": "Quality Assessment",
        "status": "processing",
        "message": "Analyzing quality metrics..."
    },
    {
        "layer": 3,
        "task_name": "Quality Assessment",
        "status": "pass",
        "message": "Quality standards met"
    },
    {
        "layer": 4,
        "task_name": "Final Verification",
        "status": "processing",
        "message": "Performing final checks..."
    },
    {
        "layer": 4,
        "task_name": "Final Verification",
        "status": "finished",
        "message": "Validation complete"
    }
]

# This would typically come from your database or processing module
parsing_document_start = {
    "layer": 1,
    "task_name": "Initialization",
    "status": "processing",
    "message": "Starting validation process"
}


async def generate_sub_event():
    """
    Simulate a sub-event generation for the validation process.
    """
    await asyncio.sleep(1)  # Simulate some processing time
    
    # Generate a sub-event
    sub_event = validation_tasks[random.randint(0, len(validation_tasks) - 1)]
    data = json.dumps(sub_event)

    yield f"data: {data}\n\n"
    


async def generate_sse_events(data: Dict[str, Any]):
    """
    Generate a stream of Server-Sent Events based on validation tasks.
    """
    # Initial notification
    yield f"data: {json.dumps(parsing_document_start)}\n\n"
    await asyncio.sleep(1)
    
    while True:
        asyncio.sleep(1)  # Simulate waiting for the next event
        async for sub_event in generate_sub_event():    
            yield sub_event