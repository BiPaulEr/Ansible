#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec={
            "name": {"type": "str", "required": True}
        }
    )

    name = module.params["name"]
    message = f"Hello, {name} !"

    module.exit_json(changed=False, message=message)

if __name__ == "__main__":
    main()

