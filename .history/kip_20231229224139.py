import requests
import sys
# Kip package manager

install_dest=r"compiler\\site_packages"
install_mgr_url="https://infdevv.github.io/kip_pgm/"


# Take args


if __name__ == "__main__":

    # If args start with install, install

    if sys.argv[1] == "install":

        # Install
        # call the install manager and get the response code

        r = requests.get(install_mgr_url+sys.argv[2])
        print(r.text)
        printn(install_mgr_url+sys.argv[2])

        if r.status_code == 200:

            # If the response code is 200, write the file
            with open((install_dest+sys.argv[2]+".py"), "w") as f:
                f.write(r.text)

        elif r.status_code == 404:
            print("Error: File not found")

        else:
            print("Error: Unknown error")

    if sys.argv[1] == "uninstall":

        # Uninstall
        # delete the file
        os.remove(install_dest+sys.argv[2]+".py") 
        print("Uninstalled")       