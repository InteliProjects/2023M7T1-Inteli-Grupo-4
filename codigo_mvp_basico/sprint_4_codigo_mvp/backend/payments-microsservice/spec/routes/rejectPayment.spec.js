const rejectPayment = require('../../src/routes/rejectPayment');

describe('rejectPayment', () => {
    it('should return a JSON response with the approved property set to true', async () => {
        const req = {};
        const res = {
            send: jest.fn(),
        };

        await rejectPayment(req, res);

        expect(res.send).toHaveBeenCalledWith({
            approved: false,
            message: 'Pagamento rejeitado. Tente novamente.',
        });
    });
});
