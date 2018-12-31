# Plan: Display antlet dependencies


# API:

## Primary features
zfs_dependencies                  - Print entire tree to screen in human readable format
zfs_dependencies -j, --json       - Print entire tree to screen in json format

## Secondary features
zfs_dependencies  antlet_name     - Print children tree for this zfs name, to screen in human readable format
zfs_dependencies  -j antlet_name  - Print children tree for this zfs name, to screen in json format
zfs_dependencies  -p antlet_name  - Print parent tree for this zfs name, to screen in human readable format
zfs_dependencies  -jp antlet_name - Print parent tree for this zfs name, to screen in json format

zfs_dependencies  zfs_name        - Print children tree for this zfs name, to screen in human readable format
zfs_dependencies  -j zfs_name     - Print children tree for this zfs name, to screen in json format
zfs_dependencies  -p zfs_name     - Print parent tree for this zfs name, to screen in human readable format
zfs_dependencies  -jp zfs_name    - Print parent tree for this zfs name, to screen in json format


# Ideal functioins

## Primary features
create_parser()
get_zfs_name_origin_list()
create_dependency_list(name_origin_list)

show_tree(dependency_list)
show_jtree(dependency_list)

## Secondary features
show_childen_tree(antlet_name, dependency_list)
show_parent_tree(antlet_name, dependency_list)
