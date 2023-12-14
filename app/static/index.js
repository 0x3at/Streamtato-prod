
function showSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.style.display = 'flex';
}
function hideSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.style.display = 'none';
}

function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
            window.location.href = "/";
        });
    }
function startPolling() {
    // Make a POST request to /home/Id to get the polling endpoint
    fetch(`/watch`, { // Use template literals to insert the Id into the URL
        method: 'POST',
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.endpoint) {
            console.log('Received polling endpoint:', data.endpoint);
            pollTaskStatus(data.endpoint); // Start polling with the received endpoint
        } else {
            console.error('Endpoint not received.');
        }
    })
    .catch((error) => {
        console.error('Error sending POST request:', error);
    });
}
    

function pollTaskStatus(endpoint) {
    console.log('Polling endpoint:', endpoint);

    function poll() {
        fetch(endpoint)
            .then((response) => response.json())
            .then((data) => {
                console.log('Received data:', data);
                if (data.state === 'SUCCESS') {
                    console.log('Task result:', data.result);
                } else if (data.state === 'FAILURE') {
                    console.log('Task failed. Traceback:', data.traceback);
                } else {
                    // Task is still pending, continue polling
                    setTimeout(poll, 1250); // Poll every 1.25 seconds (adjust as needed)
                }
            })
            .catch((error) => {
                console.error('Error polling task status:', error);
            });
    }

    // Start polling
    poll();
}

// document.addEventListener('DOMContentLoaded', function () {
//     {% for obj in objects %}
//     const buttonId = 'watch-button-{{ obj['id'] }}';
//     const buttonElement = document.getElementById(buttonId);
    
//     if (buttonElement) {
//         buttonElement.addEventListener('click', function () {
//             const id = '{{ obj['id'] }}';
//             startPolling(id);
//         });
//     }
//     {% endfor %}
// });
