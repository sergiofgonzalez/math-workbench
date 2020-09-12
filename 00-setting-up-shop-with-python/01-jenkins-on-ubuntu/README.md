# 01 &mdash; Jenkins on Ubuntu
> TBD

## Description
This sample tells you how to run Jenkins on Ubuntu bare metal, without Docker.

The LTS version can be downloaded using:

```bash
curl -LO http://mirrors.jenkins.io/war-stable/latest/jenkins.war
```

Then you can start it using:

```bash
java -jar jenkins.war
```

This will start Jenkins in interactive mode, with the configuration stored in `JENKINS_HOME` which defaults to `~/.jenkins`. This folder contains all the configuration files, plugins, jobs, and the workspace, so it is recommended to place it on a fast storage device.

Once started, you can point your browser to http://localhost:8080 to access Jenkins UI. On first run, Jenkins will ask for the initial *admin password*, which you can find in the logs and in `$JENKINS_HOME/secrets/initialAdminPassword`.

```bash
# assuming JENKINS_HOME has not been set
$ cat ~/.jenkins/secrets/initialAdminPassword
9dab6b18a6d84f9fae51a51d7aac383f
```

You will need to type that password on the *Getting Started &raquo; Unlock Jenkins* screen to proceed to the *Getting Started &raquo; Customize Jenkins* screen, on which you should select the installation of suggested plugins.

Once the plugin setup has been completed, you will be asked to create your first admin user (e.g. `jenkins`).

Right after that, you will be asked to set the Jenkins URL. There's nothing to update on the test environment, but in production you will want to set this to the URL exposed by the Load Balancer/Reverse Proxy, or to the external URL of the host if there is no lB/RP.

