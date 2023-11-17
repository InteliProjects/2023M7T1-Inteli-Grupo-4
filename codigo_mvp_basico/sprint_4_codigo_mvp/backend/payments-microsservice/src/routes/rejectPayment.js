module.exports = async (req, res) => {
    // Return a JSON with False and Payment Rejected
    res.send({
        approved: false,
        message: 'Pagamento rejeitado. Tente novamente.',
    });
};
