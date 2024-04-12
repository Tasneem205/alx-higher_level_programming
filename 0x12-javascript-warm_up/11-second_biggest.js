#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let mx = 0; let mxmx = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > mx) {
      if (parseInt(process.argv[i]) > mxmx) {
        mx = mxmx;
        mxmx = parseInt(process.argv[i]);
      } else {
        mx = parseInt(process.argv[i]);
      }
    }
  }
  console.log(mx);
}
