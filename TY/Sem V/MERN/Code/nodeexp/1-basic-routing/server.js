const http = require('http');
const url = require('url');
const fs = require('fs');
const path = require('path');

const PORT = 3001;

// Callback demonstration function
function processUserData(userData, callback) {
    console.log('Processing user data with callback...');
    
    setTimeout(() => {
        const processedData = {
            message: `Hello ${userData.name || 'Anonymous'}`,
            age: userData.age || 'Unknown',
            processedAt: new Date().toISOString()
        };
        callback(null, processedData);
    }, 500);
}

// Basic HTTP server with routing
const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const pathname = parsedUrl.pathname;
    const method = req.method;

    console.log(`${method} ${pathname}`);

    // Route 1
    if (pathname === '/' && method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(`
            <!DOCTYPE html>
            <html>
            <head>
                <title>Basic Routing Demo</title>
            </head>
            <body>
                <h1>Basic Routing with HTTP Module</h1>
                <ul>
                    <li><a href="/">Home (HTML)</a></li>
                    <li><a href="/api/users">Users API (JSON)</a></li>
                    <li><a href="/file">Static File</a></li>
                    <li><a href="/callback?name=Aaryan&age=20">Callback Demo</a></li>
                </ul>
            </body>
            </html>
        `);
    }
    // Route 2
    else if (pathname === '/api/users' && method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
            users: [
                { id: 1, name: 'Aaryan', age: 20 },
                { id: 2, name: 'Aditey', age: 20 },
                { id: 3, name: 'Aditya', age: 20 },
            ],
            message: 'JSON data from Node.js server'
        }));
    }
    // Route 3
    else if (pathname === '/file' && method === 'GET') {
        const filePath = path.join(__dirname, 'sample.html');
        fs.readFile(filePath, (err, data) => {
            if (err) {
                res.writeHead(404, { 'Content-Type': 'text/html' });
                res.end('<h1>File not found</h1>');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
    }
    // Route 4
    else if (pathname === '/callback' && method === 'GET') {
        const userData = {
            name: parsedUrl.query.name,
            age: parsedUrl.query.age
        };
        
        processUserData(userData, (error, result) => {
            if (error) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Processing failed' }));
            } else {
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify(result));
            }
        });
    }
    // Route 5
    else {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('<h1>404 - Route Not Found</h1>');
    }
});

server.listen(PORT, () => {
    console.log(`Basic Routing Server running at http://localhost:${PORT}/`);
    console.log('Demonstrates: HTTP module, routing, HTML/JSON responses, callbacks');
});

process.on('SIGINT', () => {
    console.log('\nShutting down routing server...');
    server.close(() => {
        console.log('Routing server closed.');
        process.exit(0);
    });
});