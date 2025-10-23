const express = require('express');
const router = express.Router();
const path = require('path');

router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/orders.html'));
});

router.post('/create', (req, res) => {
  const { items, totalAmount } = req.body;
  console.log('New Order Created:', { items, totalAmount });

  res.json({
    success: true,
    message: 'Order placed successfully!',
    orderId: Math.floor(Math.random() * 10000)
  });
});

module.exports = router;
