# Custom Ansible Modules Demo

This directory contains custom Ansible modules for demonstration purposes.

## Directory Structure

```
ansible/
├── library/                          # Custom modules directory
│   ├── system_info.py               # Module to collect system information
│   └── greeting_manager.py          # Module to manage greeting files
├── custom-module-demo.yaml          # Demo playbook using custom modules
└── README-CUSTOM-MODULES.md         # This file
```

## Custom Modules

### 1. system_info.py

Collects system information from target machines.

**Parameters:**
- `name` (required): Name/identifier for the system
- `hostname_only` (optional): If true, only returns hostname
- `create_file` (optional): Create a file with system info
- `file_path` (optional): Path where to create the file

**Usage Example:**
```yaml
- name: Collect system information
  system_info:
    name: "Production Server"
    hostname_only: false
    create_file: yes
    file_path: "/tmp/sysinfo.txt"
```

### 2. greeting_manager.py

Creates and manages greeting files with different styles.

**Parameters:**
- `name` (required): Name of the person to greet
- `greeting_type` (optional): Type of greeting - formal, casual, or professional
- `file_path` (optional): Where to save the greeting file
- `state` (optional): present or absent

**Usage Example:**
```yaml
- name: Create a greeting
  greeting_manager:
    name: "DevOps Team"
    greeting_type: "formal"
    file_path: "/tmp/greeting.txt"
    state: present
```

## Running the Demo

### Run the demo playbook:
```bash
ansible-playbook custom-module-demo.yaml
```

### Run with verbose output:
```bash
ansible-playbook custom-module-demo.yaml -v
```

### Run on remote hosts:
```bash
ansible-playbook -i inventory.ini custom-module-demo.yaml
```

## How Custom Modules Work

1. **Module Location**: Custom modules must be in a `library/` directory relative to your playbook
2. **Module Structure**: Written in Python using `AnsibleModule` class
3. **Parameters**: Defined using `argument_spec`
4. **Return Values**: Use `module.exit_json()` for success or `module.fail_json()` for errors
5. **Check Mode**: Supports `--check` mode for dry runs

## Module Development Best Practices

- Always validate input parameters
- Provide clear error messages
- Support check mode when possible
- Return meaningful data in results
- Handle exceptions gracefully
- Document parameters and return values

## Testing Custom Modules

Test individual modules:
```bash
# Test system_info module
ansible localhost -m system_info -a "name='Test' hostname_only=false"

# Test greeting_manager module
ansible localhost -m greeting_manager -a "name='User' greeting_type='casual'"
```

## Extending the Modules

To create your own custom module:

1. Create a new Python file in `library/` directory
2. Import `AnsibleModule` from `ansible.module_utils.basic`
3. Define your module arguments
4. Implement your module logic
5. Return results using `exit_json()` or `fail_json()`

## Requirements

- Python 3.6+
- Ansible 2.9+
- No additional Python packages required for these demo modules
