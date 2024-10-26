#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: vcenter_ovf_libraryitem
short_description: Creates a library item in content library from a virtual machine
    or virtual appliance
description: 'Creates a library item in content library from a virtual machine or
    virtual appliance. '
options:
    client_token:
        description:
        - Client-generated token used to retry a request if the client fails to get
            a response from the server. If the original request succeeded, the result
            of that request will be returned, otherwise the operation will be retried.
        - If unset, the server will create a token.
        type: str
    create_spec:
        description:
        - Information used to create the OVF package from the source virtual machine
            or virtual appliance. Required with I(state=['present'])
        - 'Valid attributes are:'
        - ' - C(name) (str): Name to use in the OVF descriptor stored in the library
            item.'
        - If unset, the server will use source's current name. (['present'])
        - ' - C(description) (str): Description to use in the OVF descriptor stored
            in the library item.'
        - If unset, the server will use source's current annotation. (['present'])
        - ' - C(flags) (list): Flags to use for OVF package creation. The supported
            flags can be obtained using ExportFlag.list.'
        - If unset, no flags will be used. (['present'])
        type: dict
    deployment_spec:
        description:
        - Specification of how the OVF package should be deployed to the target. Required
            with I(state=['deploy'])
        - 'Valid attributes are:'
        - ' - C(name) (str): Name assigned to the deployed target virtual machine
            or virtual appliance.'
        - If unset, the server will use the name from the OVF package. (['deploy'])
        - ' - C(annotation) (str): Annotation assigned to the deployed target virtual
            machine or virtual appliance.'
        - If unset, the server will use the annotation from the OVF package. (['deploy'])
        - ' - C(accept_all_EULA) (bool): Whether to accept all End User License Agreements.
            See I() ([''deploy''])'
        - '   This key is required with [''deploy''].'
        - ' - C(network_mappings) (dict): Specification of the target network to use
            for sections of type ovf:NetworkSection in the OVF descriptor. The key
            in the map is the section identifier of the ovf:NetworkSection section
            in the OVF descriptor and the value is the target network to be used for
            deployment.'
        - If unset, the server will choose a network mapping.
        - When clients pass a value of this structure as a parameter, the value in
            the field map must be the id of a resource returned by M(vmware.vmware_rest.vcenter_network_info).
            (['deploy'])
        - ' - C(storage_mappings) (dict): Specification of the target storage to use
            for sections of type vmw:StorageGroupSection in the OVF descriptor. The
            key in the map is the section identifier of the ovf:StorageGroupSection
            section in the OVF descriptor and the value is the target storage specification
            to be used for deployment. See I()'
        - If unset, the server will choose a storage mapping. (['deploy'])
        - ' - C(storage_provisioning) (str): This option defines the virtual disk
            provisioning types that can be set for a disk on the target platform.
            ([''deploy''])'
        - '   - Accepted values:'
        - '     - eagerZeroedThick'
        - '     - thick'
        - '     - thin'
        - ' - C(storage_profile_id) (str): Default storage profile to use for all
            sections of type vmw:StorageSection in the OVF descriptor.'
        - If unset, the server will choose the default profile.
        - When clients pass a value of this structure as a parameter, the field must
            be the id of a resource returned by M(vmware.vmware_rest.vcenter_storage_policies_info).
            (['deploy'])
        - ' - C(locale) (str): The locale to use for parsing the OVF descriptor.'
        - If unset, the server locale will be used. (['deploy'])
        - ' - C(flags) (list): Flags to be use for deployment. The supported flag
            values can be obtained using ImportFlag.list.'
        - If unset, no flags will be used. (['deploy'])
        - ' - C(additional_parameters) (list): Additional OVF parameters that may
            be needed for the deployment. Additional OVF parameters may be required
            by the OVF descriptor of the OVF package in the library item. Examples
            of OVF parameters that can be specified through this field include, but
            are not limited to: '
        - '   - DeploymentOptionParams'
        - '   - ExtraConfigParams'
        - '   - IpAllocationParams'
        - '   - PropertyParams'
        - '   - ScaleOutParams'
        - '   - VcenterExtensionParams'
        - ' '
        - If unset, the server will choose default settings for all parameters necessary
            for the LibraryItem.deploy operation. See LibraryItem.deploy.
        - When clients pass a value of this structure as a parameter, the field must
            contain all the attributes defined in OvfParams. (['deploy'])
        - ' - C(default_datastore_id) (str): Default datastore to use for all sections
            of type vmw:StorageSection in the OVF descriptor.'
        - If unset, the server will choose the default datastore.
        - When clients pass a value of this structure as a parameter, the field must
            be the id of a resource returned by M(vmware.vmware_rest.vcenter_datastore_info).
            (['deploy'])
        - ' - C(vm_config_spec) (dict): The I(resource_pool_deployment_spec).vm-config-spec
            is used for virtual machine configuration settings including hardware
            specifications to use in place of the OVF descriptor. If set, the OVF
            descriptor acts as a disk descriptor. Fields in the I(resource_pool_deployment_spec)
            parameters such as I(resource_pool_deployment_spec).name that overlap
            with settings in the I(resource_pool_deployment_spec).vm-config-spec are
            not overridden and will continue to be used. Similarly, storage settings
            in the I(resource_pool_deployment_spec) that affect the disks on the virtual
            machine namely I(resource_pool_deployment_spec).storage-mappings, I(resource_pool_deployment_spec).storage-profile-id,
            I(resource_pool_deployment_spec).storage-provisioning and I(resource_pool_deployment_spec).default-datastore-id
            will also be honored.'
        - If unset, the relevant virtual machine specifications in the OVF descriptor
            of the OVF template will be used. (['deploy'])
        - '   - Accepted keys:'
        - '     - provider (string): The I(vm_config_spec_provider) is used to provide
            the optional I(vm_config_spec) used when deploying an OVF template.'
        - 'Accepted value for this field:'
        - '       - C(XML)'
        - '     - xml (string): The I(xml) is a conditional configuration made available
            upon selecting the XML. It is used to pass in a vim.vm.ConfigSpec for
            a virtual machine that has been serialized to XML and base64 encoded.'
        - This field is optional and it is only relevant when the value of I(provider)
            is XML.
        type: dict
    ovf_library_item_id:
        description:
        - Identifier of the content library item containing the OVF package to be
            deployed.
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.content_library_item_info).
            Required with I(state=['deploy', 'filter'])
        type: str
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    source:
        description:
        - Identifier of the virtual machine or virtual appliance to use as the source.
            Required with I(state=['present'])
        - 'Valid attributes are:'
        - ' - C(type) (str): Type of the deployable resource.'
        - When clients pass a value of this structure as a parameter, the field must
            be one of VirtualMachine or VirtualApp. (['present'])
        - '   This key is required with [''present''].'
        - ' - C(id) (str): Identifier of the deployable resource.'
        - 'When clients pass a value of this structure as a parameter, the field must
            be an identifier for one of these resource types: VirtualMachine or VirtualApp.
            ([''present''])'
        - '   This key is required with [''present''].'
        type: dict
    state:
        choices:
        - deploy
        - filter
        - present
        default: present
        description: []
        type: str
    target:
        description:
        - Specification of the target content library and library item. This parameter
            is mandatory.
        - 'Valid attributes are:'
        - ' - C(library_id) (str): Identifier of the library in which a new library
            item should be created. This field is not used if the I(library_item_id)
            field is specified.'
        - 'This field is currently required. '
        - ' In the future, if unset, the I(library_item_id) field must be specified. '
        - ''
        - When clients pass a value of this structure as a parameter, the field must
            be the id of a resource returned by M(vmware.vmware_rest.content_library_info).
            (['present'])
        - ' - C(library_item_id) (str): Identifier of the library item that should
            be should be updated.'
        - If unset, a new library item will be created. The I(library_id) field must
            be specified if this field is set.
        - When clients pass a value of this structure as a parameter, the field must
            be the id of a resource returned by M(vmware.vmware_rest.content_library_item_info).
            (['present'])
        - ' - C(resource_pool_id) (str): Identifier of the resource pool to which
            the virtual machine or virtual appliance should be attached.'
        - When clients pass a value of this structure as a parameter, the field must
            be the id of a resource returned by M(vmware.vmware_rest.vcenter_resourcepool_info).
            (['deploy', 'filter'])
        - '   This key is required with [''deploy'', ''filter''].'
        - ' - C(host_id) (str): Identifier of the target host on which the virtual
            machine or virtual appliance will run. The target host must be a member
            of the cluster that contains the resource pool identified by I()'
        - If unset, the server will automatically select a target host from the resource
            pool if I(resource_pool_id) is a stand-alone host or a cluster with Distributed
            Resource Scheduling (DRS) enabled.
        - When clients pass a value of this structure as a parameter, the field must
            be the id of a resource returned by M(vmware.vmware_rest.vcenter_host_info).
            (['deploy', 'filter'])
        - ' - C(folder_id) (str): Identifier of the vCenter folder that should contain
            the virtual machine or virtual appliance. The folder must be virtual machine
            folder.'
        - If unset, the server will choose the deployment folder.
        - When clients pass a value of this structure as a parameter, the field must
            be the id of a resource returned by M(vmware.vmware_rest.vcenter_folder_info).
            (['deploy', 'filter'])
        required: true
        type: dict
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that runs the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.3 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.3
"""

EXAMPLES = r"""
- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster') }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore') }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources') }}"
    name: test_vm1
    guest_OS: RHEL_7_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
  register: my_vm

- name: Create a content library pointing on a NFS share
  vmware.vmware_rest.content_locallibrary:
    name: my_library_on_nfs
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    state: present
  register: nfs_lib

- name: Export the VM as an OVF on the library
  vmware.vmware_rest.vcenter_ovf_libraryitem:
    session_timeout: 2900
    source:
      type: VirtualMachine
      id: '{{ my_vm.id }}'
    target:
      library_id: '{{ nfs_lib.id }}'
    create_spec:
      name: golden_image
      description: an OVF example
      flags: []
    state: present
  register: ovf_item

- name: Get the list of items of the NFS library
  vmware.vmware_rest.content_library_item_info:
    library_id: '{{ nfs_lib.id }}'
  register: lib_items

- name: Create a new VM from the OVF
  vmware.vmware_rest.vcenter_ovf_libraryitem:
    ovf_library_item_id: '{{ (lib_items.value|selectattr("name", "equalto", "golden_image")|first).id }}'
    state: deploy
    target:
      resource_pool_id: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources') }}"
    deployment_spec:
      name: my_vm_from_ovf
      accept_all_EULA: true
      storage_provisioning: thin

- name: Create a new VM from the OVF and specify the host and folder
  vmware.vmware_rest.vcenter_ovf_libraryitem:
    ovf_library_item_id: '{{ (lib_items.value|selectattr("name", "equalto", "golden_image")|first).id }}'
    state: deploy
    target:
      resource_pool_id: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources') }}"
      folder_id: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      host_id: "{{ lookup('vmware.vmware_rest.host_moid', '/my_dc/host/my_cluster/esxi1.test/test_vm1') }}"
    deployment_spec:
      name: my_vm_from_ovf_on_a_host
      accept_all_EULA: true
      storage_provisioning: thin
"""
RETURN = r"""
# content generated by the update_return_section callback# task: Create a new VM from the OVF and specify the host and folder
value:
  description: Create a new VM from the OVF and specify the host and folder
  returned: On success
  sample:
    error:
      errors: []
      information: []
      warnings: []
    resource_id:
      id: vm-1078
      type: VirtualMachine
    succeeded: 1
  type: dict
"""


# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "filter": {
        "query": {},
        "body": {"target": "target"},
        "path": {"ovf_library_item_id": "ovf_library_item_id"},
    },
    "create": {
        "query": {"client_token": "client_token"},
        "body": {"create_spec": "create_spec", "source": "source", "target": "target"},
        "path": {},
    },
    "deploy": {
        "query": {"client_token": "client_token"},
        "body": {"deployment_spec": "deployment_spec", "target": "target"},
        "path": {"ovf_library_item_id": "ovf_library_item_id"},
    },
}  # pylint: disable=line-too-long

from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    open_session,
    prepare_payload,
    session_timeout,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["client_token"] = {"no_log": True, "type": "str"}
    argument_spec["create_spec"] = {"type": "dict"}
    argument_spec["deployment_spec"] = {"type": "dict"}
    argument_spec["ovf_library_item_id"] = {"type": "str"}
    argument_spec["source"] = {"type": "dict"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["deploy", "filter", "present"],
        "default": "present",
    }
    argument_spec["target"] = {"required": True, "type": "dict"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/vcenter/ovf/library-item").format(
        **params
    )


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _create(params, session):

    library_id = (
        params["target"]["library_id"] if "library_id" in params["target"] else None
    )
    lookup_url = f"https://{params['vcenter_hostname']}/api/content/library/item?library_id={library_id}"
    per_id_url = "https://{vcenter_hostname}/api/content/library/item".format(**params)
    uniquity_keys = None

    def comp_func(device):
        return device["value"]["name"] == params["create_spec"].get("name")

    _json = None

    if not _json and (uniquity_keys or comp_func):
        _json = await exists(
            params,
            session,
            url=lookup_url,
            uniquity_keys=uniquity_keys,
            per_id_url=per_id_url,
            comp_func=comp_func,
        )

    if _json:
        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}
        if "_update" in globals():
            params["None"] = _json["id"]
            return await globals()["_update"](params, session)

        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = ("https://{vcenter_hostname}" "/api/vcenter/ovf/library-item").format(
        **params
    )
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}

        if (resp.status in [200, 201]) and "error" not in _json:
            if isinstance(_json, str):  # 7.0.2 and greater
                _id = _json  # TODO: fetch the object
            elif isinstance(_json, dict) and "value" not in _json:
                _id = list(_json["value"].values())[0]
            elif isinstance(_json, dict) and "value" in _json:
                _id = _json["value"]
            _json_device_info = await get_device_info(session, _url, _id)
            if _json_device_info:
                _json = _json_device_info

        return await update_changed_flag(_json, resp.status, "create")


async def _deploy(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["deploy"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["deploy"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/ovf/library-item/{ovf_library_item_id}?action=deploy"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/ovf/library-item/{ovf_library_item_id}?action=deploy"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "deploy")


async def _filter(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["filter"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["filter"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/ovf/library-item/{ovf_library_item_id}?action=filter"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/ovf/library-item/{ovf_library_item_id}?action=filter"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "filter")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(current_loop)
        current_loop.run_until_complete(main())
    finally:
        current_loop.close()
