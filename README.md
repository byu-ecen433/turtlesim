# ECEN 433 - Lab 2: Using ROS with Turtlesim

Starter code for Lab 2. You will write two ROS nodes that drive and observe the
turtlesim turtle, launch them together with a launch file, and control one of
them at runtime with a ROS parameter.

The full lab instructions live on the course site. This README covers the
repository itself: how it is laid out, and how to build and run it.

## What you need to write

Parts II through IV are everything marked `TODO` in these three files:

| File | What it does |
|---|---|
| `packages/turtle_control/src/square_node.py` | Publishes `geometry_msgs/Twist` on `turtle1/cmd_vel` to drive the turtle in a repeating square. |
| `packages/turtle_control/src/direction_node.py` | Subscribes to `turtle1/pose`, works out which way the turtle is facing, and publishes it on `turtle1/direction` at a rate set by the `/direction_pub_rate` parameter. |
| `packages/turtle_control/launch/turtle_control.launch` | Starts turtlesim plus your nodes. turtlesim is already wired up; add your nodes. |

Everything else - the package, its `CMakeLists.txt` and `package.xml`, the
launcher script, the Docker setup - is done for you.

**Part V has no starter file.** You write a new node from scratch in
`packages/turtle_control/src/`, and add it plus a second turtlesim to the
launch file. You do not need to create a new package - put it in
`turtle_control` alongside the others. Remember that a new file has to be
made executable before `roslaunch` will run it.

## Building and running

Build the Docker image. Run this from the root of this repository:

```bash
dts devel build -f
```

The workspace is installed with symlinks, so **editing** an existing Python node
or launch file does not need a rebuild - save the file and launch again. Re-run
the build when you **add** a new file, rename one, or add a package, message
type, or dependency.

Then start everything:

```bash
dts devel run -X -L square
```

- `-X` allows the container to open GUI windows. Without it the turtlesim
  window never appears.
- `-L square` runs `launchers/square.sh`, which calls `roslaunch` on your
  launch file. This is the command the TAs will use to grade, so make sure it
  works with no manual steps.

To poke around inside the container instead of launching straight away:

```bash
dts devel run -X --cmd bash
```

and to attach a second terminal to a container that is already running:

```bash
dts devel run attach
```

The ROS environment is sourced automatically in every shell, so `rostopic`,
`rosnode`, and tab-completion all work as soon as you get a prompt.

## Where things live

```
packages/            your ROS packages - this is where your code goes
  turtle_control/
    src/             node executables (must be chmod +x, and end in .py)
    launch/          launch files
launchers/           bash entry points, one per runnable configuration
                       square.sh  ->  dts devel run -L square
dependencies-apt.txt apt packages installed into the image (turtlesim is here)
dependencies-py3.txt pip packages installed into the image
dtproject/           project config - see below
Dockerfile           don't edit; it reads dtproject/ for everything
```

Inside the container your code is mounted at `/code/src/turtlesim/`, and the
catkin workspace root is `/code`.

## Adding a new package

You should not need to for this lab, but if you do:

```bash
cd packages
catkin_create_pkg <package_name> rospy std_msgs geometry_msgs
```

New Python nodes must be executable or ROS will not find them:

```bash
chmod +x packages/<package_name>/src/<node_name>.py
```