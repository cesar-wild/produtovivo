const express = require('express');
const Stripe = require('stripe');

const router = express.Router();
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

const APP_URL = process.env.APP_URL || 'https://produtovivo.com';
const PRICE_ID = process.env.STRIPE_PRICE_ID;

/**
 * POST /checkout/session
 * Creates a Stripe Checkout session for the guide purchase.
 */
router.post('/session', async (req, res) => {
  try {
    const session = await stripe.checkout.sessions.create({
      mode: 'payment',
      line_items: [
        {
          price: PRICE_ID,
          quantity: 1,
        },
      ],
      payment_method_types: ['card'],
      billing_address_collection: 'auto',
      success_url: `${APP_URL}/sucesso?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${APP_URL}/#comprar`,
      metadata: {
        product: 'guia-produtovivo-v1',
      },
    });

    res.json({ url: session.url });
  } catch (err) {
    console.error('Checkout session error:', err);
    res.status(500).json({ error: 'Falha ao criar sessão de pagamento' });
  }
});

/**
 * GET /checkout/success
 * Verifies a completed session (for the success page to confirm payment).
 */
router.get('/success', async (req, res) => {
  const { session_id } = req.query;
  if (!session_id) return res.status(400).json({ error: 'session_id required' });

  try {
    const session = await stripe.checkout.sessions.retrieve(session_id);
    if (session.payment_status !== 'paid') {
      return res.status(402).json({ error: 'Payment not completed' });
    }
    res.json({ email: session.customer_details?.email, status: 'paid' });
  } catch (err) {
    console.error('Success check error:', err);
    res.status(500).json({ error: 'Falha ao verificar pagamento' });
  }
});

module.exports = router;
