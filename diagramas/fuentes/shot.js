const puppeteer = require('/home/claude/.npm-global/lib/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer');
(async()=>{const [,,inp,outp,w,h]=process.argv;const b=await puppeteer.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});
const p=await b.newPage();await p.setViewport({width:+w,height:+h,deviceScaleFactor:2});await p.goto('file://'+inp);await p.screenshot({path:outp});await b.close();})();
