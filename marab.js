const { spawn } = require('child_process');
const path = require('path');

const scriptPath = path.join(__dirname, 'marab.py');
const py = spawn('python', [scriptPath], { stdio: 'inherit' });

py.on('close', (code) => {
  process.exit(code ?? 0);
});