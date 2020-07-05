let image = {
    // A simple object to describe an image.
    filename: 'undefined',
    path: 'undefined',
    fullpath: function ()
    {
        // Just a test to print the output of an imaginary object and set it's property.
        return `${this.path}/${this.filename}`;
    },
    file_size: file_size = 0
}

// log the objects full path.
console.log(image.fullpath())



