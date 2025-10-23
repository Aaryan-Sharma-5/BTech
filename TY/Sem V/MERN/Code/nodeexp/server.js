const http = require('http');
const url = require('url');

const PORT = 3000;

// Callback demonstration function
function processUserData(name, age, callback) {
    // Simulate processing time
    setTimeout(() => {
        const result = {
            message: `Hello ${name}, you are ${age} years old`,
            timestamp: new Date().toISOString()
        };
        callback(null, result);
    }, 100);
}

// Create HTTP server using built-in http module
const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const path = parsedUrl.pathname;
    const method = req.method;

    console.log(`${method} ${path}`);

    // Basic Routing Implementation
    if (path === '/' && method === 'GET') {
        // Home route - HTML response
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(`
            <!DOCTYPE html>
            <html>
            <head>
                <title>Node.js HTTP Server</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    .route { background: #f5f5f5; padding: 10px; margin: 10px 0; }
                </style>
            </head>
            <body>
                <h1>Node.js HTTP Module Server</h1>
                <h2>Available Routes:</h2>
                <div class="route">
                    <strong>GET /</strong> - This home page (HTML)
                </div>
                <div class="route">
                    <strong>GET /api/data</strong> - JSON response
                </div>
                <div class="route">
                    <strong>GET /api/user?name=John&age=25</strong> - Callback demonstration
                </div>
                <div class="route">
                    <strong>POST /api/data</strong> - Handle POST data
                </div>
            </body>
            </html>
        `);
    } 
    else if (path === '/api/data' && method === 'GET') {
        // JSON API route
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
            message: 'This is JSON data from Node.js HTTP server',
            routes: ['/', '/api/data', '/api/user'],
            timestamp: new Date().toISOString()
        }));
    }
    else if (path === '/api/user' && method === 'GET') {
        // Callback demonstration route
        const name = parsedUrl.query.name || 'Anonymous';
        const age = parsedUrl.query.age || '0';
        
        processUserData(name, age, (error, result) => {
            if (error) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Processing failed' }));
            } else {
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify(result));
            }
        });
    }
    else if (path === '/api/data' && method === 'POST') {
        // Handle POST data
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });
        req.on('end', () => {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
                message: 'Data received',
                receivedData: body,
                length: body.length
            }));
        });
    }
    else {
        // 404 Not Found
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('<h1>404 - Route Not Found</h1>');
    }
});

server.listen(PORT, () => {
    console.log(`Main Demo Server running at http://localhost:${PORT}/`);
});

process.on('SIGINT', () => {
    console.log('\nShutting down HTTP server...');
    server.close(() => {
        console.log('Server closed.');
        process.exit(0);
    });
});