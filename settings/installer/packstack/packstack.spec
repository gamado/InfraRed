---
subparsers:
    packstack:
        help: OpenStack installation using Packstack
        groups:
            - title: Storage
              options:
                  storage:
                      type: YamlFile
                      help: Storage
                  storage-backend:
                      type: YamlFile
                      help: Storage backend

            - title: Config
              options:
                  config:
                      type: YamlFile
                      help: Packstack Configuration
                      default: default.yml

            - title: Debug
              options:
                  osdebug:
                      type: YamlFile
                      help: Install OS with DEBUG

            - title: Messaging
              options:
                  messaging:
                      type: YamlFile
                      help: Messaging
                      default rabbitmq.yml


            - title: Network
              options:
                  network:
                      type: YamlFile
                      help: Network
                      default neutron.yml
                  network-variant:
                      type: YamlFile
                      help: Network variant
                      default ml2-vxlan.yml

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
                  generate-conf-file:
                      type: str
                      help: generate configuration file (ini) containing default values and exits. This file is than can be used with the from-file argument
