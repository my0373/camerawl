let image = {
    // A simple object to describe an image.
    filename: 'undefined',
    path: 'undefined',
    fullpath: 'undefined',
    file_size: file_size = 0
}

let getFullImagePath = function (image)
{
    // Just a test to print the output of an imaginary object and set it's property.
    image.fullpath = `${image.path}/${image.filename}`;
    return image.fullpath

}

// log the objects full path.
console.log(getFullImagePath(image))


