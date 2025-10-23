const express = require('express');
const router = express.Router();
const path = require('path');

router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/products.html'));
});

router.get('/:id', (req, res) => {
    const productId = req.params.id;
    res.send(`
        <html>
            <head>
                <title>Product Details</title>
                <link rel="stylesheet" href="/css/style.css">
            </head>
            <body>
                <div class="container">
                    <h1>Product Details - ID: ${productId}</h1>
                    <p>This is a detailed view of product ${productId}</p>
                    <a href="/products">Back to Products</a>
                </div>
            </body>
        </html>
    `);
});

module.exports = router;
