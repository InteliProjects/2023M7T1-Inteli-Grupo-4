module.exports = async (req, res) => {
    // Retorn a JSON with True and Payment Approved
    res.send({ approved: true, message: 'Pagamento aprovado!' });
};
