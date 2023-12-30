import requests
import sys
# Kip package manager

install_dest=r"compiler\\site_packages"
install_mgr_url="infdevv.github.io/kip_pgm/index.php"


# Take args


if __name__ == "__main__":

    # If args start with install, install

    if sys.argv[1] == "install":

        # Install
        # call the install manager and get the response code

        r = requests.get(install_mgr_url)

        if r.status_code == 200:

            # If the response code is 200, write the file
            with open((install_dest+sys.argv[2]+".py"), "w") as f:
                f.write(r.text)

        else:
            print("Error: "+str(r.status_code))

    if sys.argv[1] == "uninstall":

        # Uninstall
        # delete the file
        os.remove(install_dest+sys.argv[2]+".py") 
        print("Uninstalled")       