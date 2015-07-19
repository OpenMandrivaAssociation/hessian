%{?_javapackages_macros:%_javapackages_macros}
Summary:        Java implementation of a binary protocol for web services 
Name:           hessian
Version:        4.0.7
Release:        8.2
Epoch:          0
License:        ASL 1.1
URL:            http://hessian.caucho.com/
Group:		Development/Java
Source0:        http://caucho.com/download/hessian-4.0.7-src.jar
Source1:        %{name}-build.xml
Source2:        http://repo1.maven.org/maven2/com/caucho/hessian/4.0.7/hessian-4.0.7.pom
Requires:       jpackage-utils >= 0:1.6
Requires:       java >= 0:1.4.2
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  tomcat-servlet-3.0-api
Requires:       jpackage-utils
Requires:       java
Requires:       tomcat-servlet-3.0-api

BuildArch:      noarch

%description
This is the Java implementation of Caucho's Hession binary transport
protocol for web services.

%package javadoc
Summary:        API documentation for %{name}
Group:		Documentation

%description javadoc
API documentation for %{name}.

%prep
%setup -q -c
cp %{SOURCE1} build.xml

%build
ant jar 
ant javadoc 

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp doc/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc apache.license

%files javadoc
%doc %{_javadocdir}/*
%doc apache.license

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:4.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:4.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:4.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Andy Grimm <agrimm@gmail.com> - 0:4.0.7-3
- Use newer tomcat

* Tue Feb 14 2012 Andy Grimm <agrimm@gmail.com> - 0:4.0.7-2
- enable javadoc, follow current guidelines

* Mon Aug 29 2011 Andy Grimm <agrimm@gmail.com> - 0:4.0.7-1
- Initial build

