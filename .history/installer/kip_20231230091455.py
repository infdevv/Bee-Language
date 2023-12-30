import requests
import sys
import os
import subprocess

# Kip package manager

install_dest=r"compiler\\site_packages\\"
install_mgr_url="https://infdevv.github.io/kip_pgm/"
compiler_url_github="https://raw.githubusercontent.com/infdevv/Bee-Language/main/compiler/index.py"



# Take args


if __name__ == "__main__":

    # If args == upgrade, upgrade

    if sys.argv[1] == "upgrade":

        # Upgrade
        # call the install manager and get the response code
        r = requests.get(compiler_url_github)
        if r.status_code == 200:

            # execute the 8th line

            new=r.text.split("\n")

            for item in new:
                if item.startswith("version="):
                    version=(item.split("=")[1])

            print(version)        
            version=432
            if (version >= 1.2):
                print("Updated")
                sys.exit(0)
            else:
                print("Updating...")    


            # If the response code is 200, write the file
            with open("index.py", "w+") as f:
                f.write(r.text)

            # Run the update.bat file
            subprocess.run("update.bat")

        elif r.status_code == 404:
            print("Error: File not found")

        print("Upgraded")
     

    # If args start with install, install

    if sys.argv[1] == "install":

        # Install
        # call the install manager and get the response code

        r = requests.get(install_mgr_url+sys.argv[2]+".py")
 

        if r.status_code == 200:

            # If the response code is 200, write the file
            with open((install_dest+sys.argv[2]+".py"), "w") as f:
                f.write(r.text)

        elif r.status_code == 404:
            print("Error: File not found")

        print("Installed")



    if sys.argv[1] == "uninstall":

        # Uninstall
        # delete the file
        os.remove(install_dest+sys.argv[2]+".py") 
        print("Uninstalled")       