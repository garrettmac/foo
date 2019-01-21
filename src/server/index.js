const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('An alligator approaches!');
});

app.listen(PORT, () => console.log('Gator app listening on port 3000!'));