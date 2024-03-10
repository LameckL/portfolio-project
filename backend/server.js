const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Define static file directory
app.use(express.static(path.join(__dirname, '../frontend')));

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

