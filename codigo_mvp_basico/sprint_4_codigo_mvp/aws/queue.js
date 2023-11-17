require('dotenv').config(); // Load environment variables from .env file

// Load the AWS SDK for Node.js
const AWS = require('aws-sdk');

// Create SQS service client
const sqs = new AWS.SQS({ apiVersion: '2012-11-05' });


// Setup the sendMessage parameter object
const params = {
  MessageBody: JSON.stringify({
    order_id: 1234,
    date: new Date().toISOString(),
  }),
  QueueUrl: `https://sqs.us-east-1.amazonaws.com/456273848159/Demo.fifo`,
  MessageGroupId: 'your-message-group-id', // Add the MessageGroupId
};

sqs.sendMessage(params, (err, data) => {
  if (err) {
    console.log('Error', err);
  } else {
    console.log('Mensagem adicionada com sucesso', data.MessageId);
  }
});
