# Ansible Role: Minio
[![Gitlab pipeline status (self-hosted)](https://git.dubzland.net/dubzland/ansible-role-minio/badges/master/pipeline.svg)](https://git.dubzland.net/dubzland/ansible-role-minio)

Installs and configures the Minio object storage server.

## Requirements

Ansible version 2.0 or higher.

## Role Variables

Available variables are listed below, along with their default values (see
    `defaults/main.yml` for more info):

### dubzland_minio_architecture

```yaml
dubzland_minio_architecture: "linux-amd64"
```

Platform minio will be running on.  Available options are `linux-amd64` and
`linux-ppc64le`.

### dubzland_minio_service_user/dubzland_minio_service_group

```yaml
dubzland_minio_service_user: "minio"
dubzland_minio_service_group: "minio"
```

User/group under which to run the service.  Also owner of the data directory.

### dubzland_minio_port

```yaml
dubzland_minio_port: 9199
```

Port minio will listen on.

### dubzland_minio_access_key/dubzland_minio_secret_key

```yaml
dubzland_minio_access_key: "super"
dubzland_minio_secret_key: "secret"
```

Access/Secret keys used during minio authentication.

## Dependencies

None

## Example Playbook

```yaml
- hosts: minio_servers
  become: yes
  roles:
  - role: dubzland.minio
```

## License

MIT

## Author

* [Josh Williams](https://codingprime.com)
