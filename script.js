// Event source instance
let eventSource = null;

document.getElementById("form").addEventListener("submit", function(e) {
    e.preventDefault();
    
    // Close any existing event source connection
    if (eventSource) {
        eventSource.close();
    }
    
    // Clear previous results
    const eventsContainer = document.getElementById("events-container");
    eventsContainer.innerHTML = "";
    
    const statusIndicator = document.getElementById("status-indicator");
    statusIndicator.textContent = "Validation in progress...";
    statusIndicator.className = "processing";
    
    // Get form data
    const formData = new FormData(this);
    const url = formData.get("url");
    
    // Log what we're sending
    console.log("Submitting validation for URL:", url);
    
    // Create SSE connection with the form data
    const queryParams = new URLSearchParams();
    queryParams.append("url", url);
    
    // For a proper SSE connection, we need to send the form data separately
    fetch("http://127.0.0.1:8000/stream", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        // Create an event source for streaming
        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        
        // Process the stream
        let buffer = "";
        
        function processStream() {
            return reader.read().then(({ done, value }) => {
                if (done) {
                    console.log("Stream complete");
                    return;
                }
                
                // Decode the chunk and add to buffer
                buffer += decoder.decode(value, { stream: true });
                
                // Process complete SSE messages
                const messages = buffer.split("\n\n");
                buffer = messages.pop() || ""; // Keep the last (potentially incomplete) message
                
                // Process each complete message
                messages.forEach(message => {
                    if (message.startsWith("data: ")) {
                        try {
                            const jsonStr = message.replace("data: ", "").trim();
                            const data = JSON.parse(jsonStr);
                            updateReport(data);
                        } catch (error) {
                            console.error("Error parsing SSE message:", error);
                        }
                    }
                });
                
                // Continue reading
                return processStream();
            });
        }
        
        // Start processing the stream
        return processStream();
    })
    .catch(error => {
        console.error("Error with validation request:", error);
        statusIndicator.textContent = "Error: " + error.message;
        statusIndicator.className = "error";
    });
});

function updateReport(data) {
    const eventsContainer = document.getElementById("events-container");
    const statusIndicator = document.getElementById("status-indicator");
    
    // Create event element
    const eventItem = document.createElement("div");
    eventItem.className = `event-item ${data.status}`;
    
    // Create event header
    const eventHeader = document.createElement("div");
    eventHeader.className = "event-header";
    
    // Add layer indicator
    const layerBadge = document.createElement("span");
    layerBadge.className = "layer-badge";
    layerBadge.textContent = `Layer ${data.layer}`;
    eventHeader.appendChild(layerBadge);
    
    // Add task name
    const taskName = document.createElement("span");
    taskName.className = "task-name";
    taskName.textContent = data.task_name;
    eventHeader.appendChild(taskName);
    
    // Add status badge
    const statusBadge = document.createElement("span");
    statusBadge.className = `status-badge ${data.status}`;
    statusBadge.textContent = data.status.toUpperCase();
    eventHeader.appendChild(statusBadge);
    
    eventItem.appendChild(eventHeader);
    
    // Add message
    if (data.message) {
        const message = document.createElement("div");
        message.className = "event-message";
        message.textContent = data.message;
        eventItem.appendChild(message);
    }
    
    // Add sub-task if present
    if (data.sub_task_name) {
        const subTask = document.createElement("div");
        subTask.className = "sub-task";
        subTask.textContent = `Sub-task: ${data.sub_task_name}`;
        eventItem.appendChild(subTask);
    }
    
    // Add details if present
    if (data.data) {
        const details = document.createElement("div");
        details.className = "event-details";
        details.textContent = JSON.stringify(data.data, null, 2);
        eventItem.appendChild(details);
    }
    
    // Add to container
    eventsContainer.prepend(eventItem);
    
    // Update status indicator if this is a finished event
    if (data.status === "finished") {
        statusIndicator.textContent = "Validation complete";
        statusIndicator.className = "finished";
    }
}
