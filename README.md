iai_cad_tools
=============

A collection of tools to work with or manage CAD models.

## Downloading CAD models
The IAI group shares and versions CAD models via a central svn 
server. The ROS package `iai_cad_downloader` holds a python script
`download_cad_models` which downloads a set of subdirectories from that
CAD model svn server. 

In addition to a list of subdirectories to download, `download_cad_models`
accepts optional command line arguments to change the remote checkout
server address and local storage directory. By default, the svn server
is the address of the IAI server, and the local storage directory equals
to `./meshes`. 

Example usage via ROS:
```shell
roscd my_app
rosrun iai_cad_downloader download-cad-models.py outdoor kitchen/food-drinks
```
This will checkout the subdirs `outdoor` and `kitchen/food-drinks` from
theserver into `my_app/meshes/outdoor` and `my_app/meshes/kitchen/food-drinks`.

To put the checkouts into a different local directory `models` run:
```shell
rosrun iai_cad_downloader download-cad-models.py -d models outdoor kitchen/food-drinks
```

In case you want to access models from a different svn server, execute:
```shell
rosrun iai_cad_downloader download_cad_models.py -s <some_svn_address> my-cad-subdir
```
