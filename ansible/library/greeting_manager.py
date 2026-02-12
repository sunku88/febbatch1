#!/usr/bin/python
# -*- coding: utf-8 -*-

# Custom Ansible Module - Greeting Manager
# This module creates and manages greeting files

from ansible.module_utils.basic import AnsibleModule
import os
from datetime import datetime

def create_greeting(name, greeting_type, file_path):
    """Create a greeting file"""
    greetings = {
        'formal': f"Dear {name},\n\nWe hope this message finds you well.\n\nBest regards,\nAnsible Automation Team",
        'casual': f"Hey {name}!\n\nHope you're having a great day!\n\nCheers,\nAnsible Bot",
        'professional': f"Hello {name},\n\nThank you for using our automation system.\n\nSincerely,\nAutomation System"
    }
    
    content = greetings.get(greeting_type, greetings['formal'])
    content += f"\n\n---\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    return content

def main():
    module_args = dict(
        name=dict(type='str', required=True),
        greeting_type=dict(type='str', required=False, default='formal', 
                          choices=['formal', 'casual', 'professional']),
        file_path=dict(type='str', required=False, default='/tmp/greeting.txt'),
        state=dict(type='str', required=False, default='present', 
                  choices=['present', 'absent'])
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    name = module.params['name']
    greeting_type = module.params['greeting_type']
    file_path = module.params['file_path']
    state = module.params['state']

    result = {
        'changed': False,
        'name': name,
        'file_path': file_path
    }

    try:
        file_exists = os.path.exists(file_path)

        if state == 'present':
            if not module.check_mode:
                content = create_greeting(name, greeting_type, file_path)
                with open(file_path, 'w') as f:
                    f.write(content)
            
            result['changed'] = True if not file_exists else False
            result['message'] = f"Greeting file created for {name}"
            result['greeting_type'] = greeting_type

        elif state == 'absent':
            if file_exists:
                if not module.check_mode:
                    os.remove(file_path)
                result['changed'] = True
                result['message'] = f"Greeting file removed"
            else:
                result['message'] = f"Greeting file does not exist"

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=f"Error managing greeting file: {str(e)}")

if __name__ == '__main__':
    main()
