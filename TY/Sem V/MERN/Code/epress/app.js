const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

const signupRoutes = require('./routes/signup');
const productsRoutes = require('./routes/products');
const ordersRoutes = require('./routes/orders');
const employeeRoutes = require('./routes/employee');
const imagesRoutes = require('./routes/images');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, 'public')));

app.use('/images', express.static(path.join(__dirname, 'public/images')));
app.use('/css', express.static(path.join(__dirname, 'public/css')));
app.use('/js', express.static(path.join(__dirname, 'public/js')));
app.use('/data', express.static(path.join(__dirname, 'public/data')));

app.use('/', signupRoutes);
app.use('/products', productsRoutes);
app.use('/orders', ordersRoutes);
app.use('/employee', employeeRoutes);
app.use('/images-demo', imagesRoutes);

app.use((req, res) => {
    res.status(404).send(`
        <html>
            <head>
                <title>404 - Page Not Found</title>
                <link rel="stylesheet" href="/css/style.css">
            </head>
            <body>
                <div class="container">
                    <h1>404 - Page Not Found</h1>
                    <p>The page you are looking for does not exist.</p>
                    <a href="/">Go to Homepage</a>
                </div>
            </body>
        </html>
    `);
});

app.listen(PORT, () => {
    console.log(`Grocery Delivery App Server Started`);
    console.log(`Server running at: http://localhost:${PORT}`);
    console.log(`Homepage: http://localhost:${PORT}/`);
    console.log(`Products: http://localhost:${PORT}/products`);
    console.log(`Orders: http://localhost:${PORT}/orders`);
    console.log(`Employees: http://localhost:${PORT}/employee`);
    console.log(`Images Demo: http://localhost:${PORT}/images-demo`);
    console.log(`JSON Data: http://localhost:${PORT}/data/employees.json`);
});

module.exports = app;
