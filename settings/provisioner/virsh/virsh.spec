---
subparsers:
    virsh:
        help: Provision systems using virsh
        groups:
            - title: host
              options:
                  host:
                      type: str
                      help: Address/FQDN of the BM hypervisor
                  ssh-user:
                      type: str
                      help: User to SSH to the host with
                  ssh-key:
                      type: str
                      help: "User's SSH key"
            - title: image
              options:
                  image-file:
                      type: str
                      help: An image to provision the host with
                  image-server:
                      type: str
                      help: Base URL of the image file server
            - title: topology
              options:
                  network:
                      type: str
                      help: Network
                  topology:
                      type: str
                      help: 'Provision topology (default: __DEFAULT__)'
            - title: common
              options:
                  dry-run:
                      action: store_true
                      help: Only generate settings, skip the playbook execution stage
                  cleanup:
                      action: store_true
                      help: Clean given system instead of provisioning a new one
                  input:
                      action: append
                      type: str
                      short: i
                      help: Input settings file to be loaded before the merging of user args
                  output:
                      type: str
                      short: o
                      help: 'File to dump the generated settings into (default: stdout)'
                  extra-vars:
                      action: append
                      short: e
                      help: Extra variables to be merged last
                      type: str
                  from-file:
                      type: IniFile
                      help: the ini file with the list of arguments
