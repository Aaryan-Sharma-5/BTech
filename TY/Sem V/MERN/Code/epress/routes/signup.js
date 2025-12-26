const express = require('express');
const router = express.Router();
const path = require('path');

router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/signup.html'));
});

router.post('/signup', (req, res) => {
    const { name, email, password } = req.body;
    console.log('New User Signup:', { name, email });
    res.send(`
        <html>
            <head>
                <title>Signup Successful</title>
                <link rel="stylesheet" href="/css/style.css">
            </head>
            <body>
                <div class="container">
                    <div class="success-message">
                        <h1>Signup Successful!</h1>
                        <p>Welcome, ${name}!</p>
                        <p>Your account has been created successfully.</p>
                        <p>Email: ${email}</p>
                        <div style="margin-top: 20px;">
                            <a href="/" class="btn">Back to Home</a>
                            <a href="/products" class="btn btn-primary">Browse Products</a>
                        </div>
                    </div>
                </div>
            </body>
        </html>
    `);
});

module.exports = router;
