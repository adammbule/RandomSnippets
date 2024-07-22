const WebSocket = require('ws');
const socket = new WebSocket("wss:///ws-pa/getquotes");

let options = []; // Array to store the options

socket.onopen = function(event) {
    console.log("WebSocket connection established");
    // Send a message once connected
    socket.send(JSON.stringify({
        "member": {
            "dob": 4,
            "mob": 10,
            "yob": 1997
        },
        "ModuleID": "adam-bym-0425c66a-e47a-4471-a243-d0cc592661e3"
    }));
};

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);

    // Check if the message contains a Payload
    if (data && data.Payload) {
        let option = {}; // Object to store current option details

        // Check for quoteNo
        if (data.Payload.quoteNo) {
            option.quoteNumber = data.Payload.quoteNo;
        } else {
            option.quoteNumber = "No quote number found";
        }

        // Check for periodicRates
        if (data.Payload.periodicRates !== undefined) {
            option.periodicRates = data.Payload.periodicRates;
        } else {
            option.periodicRates = "No periodic rates found";
        }

        // Check for benefits
        if (data.Payload.benefits !== undefined) {
            option.benefits = data.Payload.benefits;
        } else {
            option.benefits = "No benefits found";
        }

        // Push the current option into the options array
        options.push(option);

        // Save to specific attributes option1, option2, option3 if there are three options
        if (options.length === 3) {
            const [option1, option2, option3] = options;
            console.log("Option 1:", option1);
            console.log("Option 2:", option2);
            console.log("Option 3:", option3);
            // Further processing or saving to other attributes can be done here
            // For example:
            // saveToSomeOtherAttribute(option1, option2, option3);
            
            // Clear options array for next set of data
            options = [];
        }
    } else {
        console.log("No Payload found in the message.");
    }
};

socket.onerror = function(error) {
    console.error("WebSocket error:", error);
};

socket.onclose = function(event) {
    console.log("WebSocket connection closed");
};

// Close the WebSocket connection after some time
setTimeout(function() {
    socket.close();
}, 3000); // Close after 60 seconds
