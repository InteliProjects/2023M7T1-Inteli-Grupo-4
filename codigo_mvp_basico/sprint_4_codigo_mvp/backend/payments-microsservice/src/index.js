const express = require('express');
const app = express();
const approvePayment = require('./routes/approvePayment');
const rejectPayment = require('./routes/rejectPayment');

app.use(express.json());
app.use(express.static(__dirname + '/static'));

app.get('/approve', approvePayment);
app.get('/reject', rejectPayment);

app.listen(3000, () => console.log('Listening on port 3000'));

const gracefulShutdown = () => {
    db.teardown()
        .catch(() => {})
        .then(() => process.exit());
};

process.on('SIGINT', gracefulShutdown);
process.on('SIGTERM', gracefulShutdown);
process.on('SIGUSR2', gracefulShutdown); // Sent by nodemon
