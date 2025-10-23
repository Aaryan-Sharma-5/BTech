const fs = require('fs');
const path = require('path');

console.log('Blocking vs Non-blocking Operations Demo\n');

const demoFile = path.join(__dirname, 'test.txt');
const content = 'This is test content for blocking vs non-blocking demo.\n'.repeat(100);

try {
    fs.writeFileSync(demoFile, content);
    console.log('Demo file created\n');
} catch (error) {
    console.error('Error creating file:', error.message);
}

console.log('1. BLOCKING OPERATIONS');
console.time('Blocking read');
try {
    const data = fs.readFileSync(demoFile, 'utf8');
    console.log(`File read synchronously - Size: ${data.length} characters`);
} catch (error) {
    console.error('Blocking read error:', error.message);
}
console.timeEnd('Blocking read');
console.log('Main thread was blocked during file read\n');

console.log('2. NON-BLOCKING OPERATIONS');
console.time('Non-blocking read');
fs.readFile(demoFile, 'utf8', (err, data) => {
    if (err) {
        console.error('Non-blocking read error:', err.message);
        return;
    }
    console.log(`File read asynchronously - Size: ${data.length} characters`);
    console.timeEnd('Non-blocking read');

    cleanup();
});

function cleanup() {
    try {
        fs.unlinkSync(demoFile);
        console.log('\nDemo file cleaned up');
    } catch (error) {
        console.error('Cleanup error:', error.message);
    }
}

module.exports = {
    demonstrateBlocking: () => {
        const data = fs.readFileSync(demoFile, 'utf8');
        return data.length;
    },
    demonstrateNonBlocking: (callback) => {
        fs.readFile(demoFile, 'utf8', (err, data) => {
            if (err) return callback(err);
            callback(null, data.length);
        });
    }
};