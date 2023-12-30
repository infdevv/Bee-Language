<<<<<<< HEAD
// Ahh, yes javascript, this is the runner.

// look for the temp/js_data.txt file

// Get le modules
var fs = require('fs');

// Read the file
code = fs.readFileSync('temp/js_data.txt', 'utf8');

console.log("Swapped to Javascript");

=======
// Ahh, yes javascript, this is the runner.

// look for the temp/js_data.txt file

// Get le modules
var fs = require('fs');

// Read the file
code = fs.readFileSync('temp/js_data.txt', 'utf8');

console.log("Swapped to Javascript");

>>>>>>> d0093f1bb9125b9712876461e1aca009846b1ded
eval(code)