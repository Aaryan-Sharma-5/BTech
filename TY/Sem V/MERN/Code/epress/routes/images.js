const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Image Serving Demo - All Types</title>
            <link rel="stylesheet" href="/css/style.css">
        </head>
        <body>
            <div class="navbar">
                <div class="container">
                    <h2>Fresh Grocery Delivery</h2>
                    <nav>
                        <a href="/">Home</a>
                        <a href="/products">Products</a>
                        <a href="/orders">Orders</a>
                        <a href="/employee">Employees</a>
                        <a href="/images-demo">Images Demo</a>
                    </nav>
                </div>
            </div>

            <div class="container">
                <h1>Image Serving Demonstration</h1>
                <p class="subtitle">Express.js can serve ANY type of image format</p>

                <h2>Example Image Formats</h2>
                <div class="image-demo-grid">
                    <div class="demo-card">
                        <h3>JPG / JPEG</h3>
                        <p><strong>Extension:</strong> .jpg, .jpeg</p>
                        <p><strong>Access URL:</strong></p>
                        <code>/images/sample.jpg</code>
                    </div>

                    <div class="demo-card">
                        <h3>PNG</h3>
                        <p><strong>Extension:</strong> .png</p>
                        <p><strong>Access URL:</strong></p>
                        <code>/images/sample.png</code>
                    </div>
                </div>
            </div>

            <footer>
                <p>&copy; 2025 Fresh Grocery Delivery. All rights reserved.</p>
            </footer>
        </body>
        </html>
    `);
});

module.exports = router;
