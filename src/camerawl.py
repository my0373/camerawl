from camerawl.repo import ImageRepo, ImagePath


if __name__ == '__main__':

    # The location where we can reliably find the photos.
    # TODO: Replace this with a .env file or a config file,
    #       or something that isn't a hardcoded hack.
    photodir = "/Users/myork/"

    # filetypes we will match
    #filter = ["raw"]
    #refilter re.compile(filter)

    # Define the path we want to scan
    ip = ImagePath(photodir)

    # Create a repository using the path above.
    ir = ImageRepo(ip)

    print(ir.scan())