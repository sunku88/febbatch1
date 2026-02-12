#!/usr/bin/python
# -*- coding: utf-8 -*-

# Custom Ansible Module - System Info Collector
# This is a demo custom module that gathers system information

from ansible.module_utils.basic import AnsibleModule
import socket
import platform
import os

def get_system_info(hostname_only=False):
    """Collect system information"""
    info = {
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'platform_version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor(),
        'python_version': platform.python_version()
    }
    
    if hostname_only:
        return {'hostname': info['hostname']}
    
    return info

def main():
    # Define module arguments
    module_args = dict(
        name=dict(type='str', required=True),
        hostname_only=dict(type='bool', required=False, default=False),
        create_file=dict(type='bool', required=False, default=False),
        file_path=dict(type='str', required=False, default='/tmp/system_info.txt')
    )

    # Initialize the module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get module parameters
    name = module.params['name']
    hostname_only = module.params['hostname_only']
    create_file = module.params['create_file']
    file_path = module.params['file_path']

    # Collect system information
    try:
        sys_info = get_system_info(hostname_only)
        
        result = {
            'changed': False,
            'message': f'System information collected for {name}',
            'system_info': sys_info
        }

        # Create file if requested
        if create_file and not module.check_mode:
            try:
                with open(file_path, 'w') as f:
                    f.write(f"System Information Report for {name}\n")
                    f.write("=" * 50 + "\n\n")
                    for key, value in sys_info.items():
                        f.write(f"{key.replace('_', ' ').title()}: {value}\n")
                result['changed'] = True
                result['file_created'] = file_path
            except Exception as e:
                module.fail_json(msg=f"Failed to create file: {str(e)}")

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=f"Error collecting system info: {str(e)}")

if __name__ == '__main__':
    main()
