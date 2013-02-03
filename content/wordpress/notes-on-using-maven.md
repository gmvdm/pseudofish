Title: Notes on using Maven
Date: 2011-03-14 03:38
Author: gmwils
Category: Technology

I've been looking at build tools for JVM projects. These are the notes I
took while reviewing [Maven][].

-   `mvn install`
-   `mvn site` - generate a summary of the project
-   `mvn dependency:analyze` - determine missing or unused dependencies
-   `mvn dependency:tree` - tree view of dependencies
-   `mvn help:effective-pom` - useful for debugging

### Refactoring Maven Projects

For a given Maven project, these are some strategies to optimise the
process. Mostly this is the DRY principle - Don't Repeat Yourself.

-   Pull up common dependencies to "dependencyManagement", then only
    refer to groupId:artifactId in the child project
-   Use built-ins `${project.version}` and `${project.groupId}` when
    referring to a sibling project
-   Use properties to re-factor version numbers across multiple
    dependencies from the same group

### Build profiles

Use build profiles to setup different environments for
dev/test/staging/production

-   Specify profiles as the last things in a POM
-   Call using -P e.g. mvn clean install -Pproduction -X
-   Activation parameters automatically select a profile based on a set
    of selectors. (ie. a JDK6 profile if JDK6 is used)
-   Profiles can be stored in a separate "profiles.xml" that lives next
    to "pom.xml"
-   `mvn help:active-profiles`
-   You can set a default profile in your `~/.m2/settings.xml` and put
    passwords into settings files as well

### Finding bundles

There is an online repository at [http://mvnrepository.com/][]

### Maven Properties

-   **project.\*** – Maven Project Object Model, that is stuff in your
    pom.xml. See:
    http://maven.apache.org/ref/2.2.1/maven-model/maven.html
-   **settings.\*** – Things from your \~/.m2/settings.xml file. See:
    [online docs][]
-   **env.\*** – Environment variables, such as PATH, HOME, JAVA\_HOME
    and M2\_HOME. Note: prefer ${user.home} to ${env.HOME}
-   **System properties** – things from System.getProperty(), such as
    java.version, java.home, os.name, os.arch, user.dir, user.home, etc.
-   **User defined** – arbitrary properties within your pom.xml

Note: you can use maven properties in resource files, such as a
.properties or .xml file under src/main/resources.

You need to enable this in the pom.xml:

    :::xml
    <build>
      <resources>
        <resource>src/main/resources</resource>
        <filtering>true</filtering>
      </resources>
    </build>

Assigning custom properties per profile can help with deployment into
multiple environments.

### Maven & Eclipse

Eclipse has very good integration for Maven. Later versions of Eclipse
include this in their package. It can also be added from
[http://m2eclipse.codehaus.org/][]

### Maven Archetypes

Archetypes exist for a range of different project types.

    mvn archetype:generate

Custom archetypes can be developed if you have a new type of [project][]
or generated from an existing [project][1].

### Maven sites

Maven can generate a site for your project showing information about the
project and various reports.


    mvn archetype:create -DgroupId=com.example -DartifactId=sample-project
    cd sample-project
    mvn site:run
    mvn clean site
    mvn site:run
    mvn clean site-deploy

### Repository Manager

Hosting a local repository for a team provides a number of benefits,
including a local cache to avoid excessive network usage. Additionally,
work can be shared both internally and externally.

A repository can be as simple as a file system with the appropriate
layout, or a full [repository][] [manager][]. Nexus is an option for
hosting a repository. It can be downloaded from:
[http://nexus.sonatype.org/download-nexus.html][]

### Other Resources

-   [Cheat sheet][] – comprehensive list of useful commands.
-   [Maven - The Definitive Guide][]
-   [Various Books][]
-   [Using Maven with Clojure][]

Note: I'm continuing with [lein][] for my clojure projects. To integrate
with Maven, you can generate a pom.xml file for a with "`lein pom`".

  [Maven]: http://maven.apache.org/
  [http://mvnrepository.com/]: http://mvnrepository.com/
  [online docs]: http://maven.apache.org/ref/2.2.1/maven-settings/settings.html
  [http://m2eclipse.codehaus.org/]: http://m2eclipse.codehaus.org/
  [project]: http://maven.apache.org/guides/mini/guide-creating-archetypes.html
  [1]: http://maven.apache.org/archetype/maven-archetype-plugin/create-from-project-mojo.html
  [repository]: http://maven.apache.org/guides/introduction/introduction-to-repositories.html
  [manager]: http://maven.apache.org/repository-management.html
  [http://nexus.sonatype.org/download-nexus.html]: http://nexus.sonatype.org/download-nexus.html
  [Cheat sheet]: http://nbtconsulting.com/cheat-sheets/maven-cheat-sheet.html
  [Maven - The Definitive Guide]: http://www.amazon.com/Maven-Definitive-Guide-Sonatype-Company/dp/0596517335/ref=sr_1_1?ie=UTF8&qid=1299666613&sr=8-1
  [Various Books]: http://www.sonatype.com/books.html
  [Using Maven with Clojure]: http://cemerick.com/2010/03/25/why-using-maven-for-clojure-builds-is-a-no-brainer/
  [lein]: http://alexott.net/en/clojure/ClojureLein.html
