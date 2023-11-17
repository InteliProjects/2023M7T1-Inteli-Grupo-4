const approvePayment = require('../../src/routes/approvePayment');

describe('approvePayment', () => {
    it('should return a JSON response with the approved property set to true', async () => {
        const req = {};
        const res = {
            send: jest.fn(),
        };

        await approvePayment(req, res);

        expect(res.send).toHaveBeenCalledWith({
            approved: true,
            message: 'Pagamento aprovado!',
        });
    });
});
