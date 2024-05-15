document.addEventListener("DOMContentLoaded", () => {
    const backendCode = `
      // app.js
      const express = require('express');
      const app = express();
      app.get('/', (req, res) => res.send('Hello world!'));
      const port = process.env.PORT || 8082;
      app.listen(port, () => console.log(\`Server running on port \${port}\`));
    `;
  
    const frontendCode = `
      // App.js
      import React from 'react';
      import ReactDOM from 'react-dom';
      ReactDOM.render(<h1>Hello, world!</h1>, document.getElementById('root'));
    `;
  
    document.getElementById("backendCode").textContent = backendCode;
    document.getElementById("frontendCode").textContent = frontendCode;
  });