%{?scl:%scl_package maven-enforcer}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-enforcer
Version:        1.4.1
Release:        5.2%{?dist}
Summary:        Maven Enforcer
License:        ASL 2.0
URL:            http://maven.apache.org/enforcer
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/enforcer/enforcer/%{version}/enforcer-%{version}-source-release.zip

Patch0:         0001-Port-to-Maven-3-API.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(com.google.code.findbugs:jsr305)
BuildRequires:  %{?scl_prefix}mvn(commons-lang:commons-lang)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-compat)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  %{?scl_prefix}mvn(org.beanshell:bsh)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)

%description
Enforcer is a build rule execution framework.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%package api
Summary:        Enforcer API

%description api
This component provides the generic interfaces needed to
implement custom rules for the maven-enforcer-plugin.

%package rules
Summary:        Enforcer Rules

%description rules
This component contains the standard Enforcer Rules.

%package plugin
Summary:        Enforcer Rules

%description plugin
This component contains the standard Enforcer Rules.

%prep
%setup -q -n enforcer-%{version}
%patch0 -p1

# Replace plexus-maven-plugin with plexus-component-metadata
sed -e "s|<artifactId>plexus-maven-plugin</artifactId>|<artifactId>plexus-component-metadata</artifactId>|" \
    -e "s|<goal>descriptor</goal>|<goal>generate-metadata</goal>|" \
    -i enforcer-{api,rules}/pom.xml

%build
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-enforcer
%doc LICENSE NOTICE

%files api -f .mfiles-enforcer-api
%doc LICENSE NOTICE

%files rules -f .mfiles-enforcer-rules

%files plugin -f .mfiles-maven-enforcer-plugin

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.4.1-5.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.4.1-5.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-3
- Fix Maven 3 patch

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-2
- Port to Maven 3 API

* Mon Aug 31 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-1
- Update to upstream version 1.4.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-4
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-3
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-1
- Update to upstream version 1.3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-6
- Build with xmvn
- Update to current packaging guidelines

* Fri Apr 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-5
- Remove BR on maven-doxia
- Resolves: rhbz#915611

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec  6 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-2
- Add mising R: forge-parent

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Fri Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 1.1.1-3
- Including LICENSE and NOTICE

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-2
- Remove RPM bug workaround

* Fri Oct 12 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-1
- Update to upstream version 1.1.1
- Convert patches to POM macro
- Remove patch for bug 748074, upstreamed

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Jaromir Capik <jcapik@redhat.com> - 1.0.1-4
- Migration to plexus-containers-component-metadata
- Maven3 compatibility patches
- Minor spec file changes according to the latest guidelines

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Jaromir Capik <jcapik@redhat.com> - 1.0.1-2
- Removal of plexus-maven-plugin dependency (not needed)

* Tue Jun 28 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-1
- Update to latest upstream 1.0.1.
- Adapt to current guidelines.

* Thu Mar 10 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-1
- Update to latest upstream (1.0)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.2.b2
- Fix FTBFS (#631388)
- Use new maven plugin names
- Versionless jars & javadocs

* Wed May 19 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.1.b2
- Initial package
