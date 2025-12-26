const fs = require('fs');
const path = require('path');
const readline = require('readline');
const http = require('http');

console.log('File Operations Demonstration\n');

const testFile = path.join(__dirname, 'demo.txt');
function createDemoFile() {
    const content = `Line 1: Welcome to file operations
Line 2: This demonstrates file handling
Line 3: Using Node.js built-in fs module
Line 4: Check permissions and existence
Line 5: Count lines in this file
Line 6: Read file line by line
Line 7: View through browser
Line 8: End of demo file`;

    try {
        fs.writeFileSync(testFile, content);
        console.log('Demo file created: demo.txt\n');
    } catch (error) {
        console.error('Error creating demo file:', error.message);
    }
}

function checkPermissions(filePath) {
    console.log('1. CHECK PERMISSIONS');
    try {
        fs.accessSync(filePath, fs.constants.F_OK);
        console.log(`File exists: ${filePath}`);

        try {
            fs.accessSync(filePath, fs.constants.R_OK);
            console.log('Readable: YES');
        } catch {
            console.log('Readable: NO');
        }

        try {
            fs.accessSync(filePath, fs.constants.W_OK);
            console.log('Writable: YES');
        } catch {
            console.log('Writable: NO');
        }

    } catch (error) {
        console.log('File does not exist or no access');
    }
    console.log();
}

function checkFileExists(filePath) {
    console.log('2. CHECK FILE EXISTENCE');
    const exists = fs.existsSync(filePath);
    console.log(`File: ${path.basename(filePath)}`);
    console.log(`Exists: ${exists ? 'YES' : 'NO'}`);
    console.log();
}

function countLines(filePath) {
    console.log('3. COUNT LINES');
    if (!fs.existsSync(filePath)) {
        console.log('File not found');
        return;
    }

    try {
        const content = fs.readFileSync(filePath, 'utf8');
        const lines = content.split('\n');
        console.log(`File: ${path.basename(filePath)}`);
        console.log(`Total lines: ${lines.length}`);
    } catch (error) {
        console.error('Error counting lines:', error.message);
    }
    console.log();
}

async function readLineByLine(filePath) {
    console.log('4. READ LINE BY LINE');
    if (!fs.existsSync(filePath)) {
        console.log('File not found');
        return;
    }

    try {
        const fileStream = fs.createReadStream(filePath);
        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });

        let lineNumber = 0;
        for await (const line of rl) {
            lineNumber++;
            console.log(`Line ${lineNumber}: ${line}`);
        }
        console.log(`Finished reading ${lineNumber} lines`);
    } catch (error) {
        console.error('Error reading line by line:', error.message);
    }
    console.log();
}

function createBrowserViewer() {
    console.log('5. BROWSER FILE VIEWER');
    const PORT = 3002;

    const server = http.createServer((req, res) => {
        if (req.url === '/') {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(`
                <!DOCTYPE html>
                <html>
                <head>
                    <title>File Viewer</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 20px; }
                        .file-content { background: #f5f5f5; padding: 15px; white-space: pre-wrap; font-family: monospace; }
                    </style>
                </head>
                <body>
                    <h1>File Content Viewer</h1>
                    <p><a href="/view-file">View demo.txt</a></p>
                </body>
                </html>
            `);
        } else if (req.url === '/view-file') {
            fs.readFile(testFile, 'utf8', (err, data) => {
                if (err) {
                    res.writeHead(404, { 'Content-Type': 'text/html' });
                    res.end('<h1>File not found</h1>');
                    return;
                }

                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(`
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>File Content</title>
                        <style>
                            body { font-family: Arial, sans-serif; margin: 20px; }
                            .file-content { background: #f5f5f5; padding: 15px; white-space: pre-wrap; font-family: monospace; border: 1px solid #ddd; }
                        </style>
                    </head>
                    <body>
                        <h1>File: demo.txt</h1>
                        <div class="file-content">${data}</div>
                        <p><a href="/">Back to Home</a></p>
                    </body>
                    </html>
                `);
            });
        } else {
            res.writeHead(404, { 'Content-Type': 'text/html' });
            res.end('<h1>404 - Not Found</h1>');
        }
    });

    server.listen(PORT, () => {
        console.log(`File viewer server running at http://localhost:${PORT}/`);
        console.log('You can view file content through your browser');
    });

    return server;
}

async function runDemo() {
    createDemoFile();
    checkPermissions(testFile);
    checkFileExists(testFile);
    countLines(testFile);
    await readLineByLine(testFile);

    const server = createBrowserViewer();
    process.on('SIGINT', () => {
        console.log('\nShutting down file operations demo...');
        server.close(() => {
            console.log('Server closed.');
            process.exit(0);
        });
    });
}

module.exports = {
    checkPermissions,
    checkFileExists,
    countLines,
    readLineByLine,
    createBrowserViewer
};

if (require.main === module) {
    runDemo().catch(console.error);
}