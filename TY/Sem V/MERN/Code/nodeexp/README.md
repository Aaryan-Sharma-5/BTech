# Node.js Functionality Demonstrations

Simple and focused demonstrations of core Node.js concepts.

## Requirements Covered

### 1. Basic Routing
- ✅ HTTP module server creation  
- ✅ HTML and JSON responses
- ✅ Callback demonstrations

### 2. File Operations
- ✅ Check file/directory permissions
- ✅ Check file existence
- ✅ Count lines in text file
- ✅ Read file line by line
- ✅ View file content through browser

### 3. Custom Modules
- ✅ Mathematics functions module
- ✅ Module creation and export
- ✅ Module usage demonstration

### 4. Blocking vs Non-blocking
- ✅ Synchronous operations
- ✅ Asynchronous operations
- ✅ Performance comparison

## Running the Demonstrations

### Main Server (HTTP Module + Routing)
```bash
npm start
# or
node server.js
```
Access: http://localhost:3000

### Individual Demos
```bash
# Basic Routing
npm run routing

# File Operations
npm run file-ops

# Custom Modules
npm run custom-module

# Blocking vs Non-blocking
npm run blocking
```

## Files Structure
```
nodeexp/
├── server.js                    # Main HTTP server with routing
├── 1-basic-routing/
│   ├── server.js               # Routing server
│   └── sample.html             # Static file
├── 2-file-operations/
│   └── file-operations.js      # File system demos
├── 3-custom-modules/
│   ├── math-module.js          # Custom math module
│   └── demo.js                 # Module usage
└── 4-blocking-nonblocking/
    └── demo.js                 # Async vs sync demo
```

## Key Features

**Simplified and focused** - Only essential functionality  
**No unnecessary complexity** - Clean, readable code  
**Working demonstrations** - All features tested  
**Educational** - Clear examples of each concept