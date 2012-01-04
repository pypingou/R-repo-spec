%global packname  Runiversal
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Runiversal - Package for converting R objects to Java variables and XML.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains some functions for converting R objects to Java
style variables and XML. Generated Java code is interpretable by dynamic
Java libraries such as Beanshell. Calling R externally and handling the
Java or XML output is an other way to call R from other languages without
native interfaces. For a Java implemantion of this approach visit

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/Runiversal/DESCRIPTION
%doc %{rlibdir}/Runiversal/html
%{rlibdir}/Runiversal/R
%{rlibdir}/Runiversal/INDEX
%{rlibdir}/Runiversal/Meta
%{rlibdir}/Runiversal/NAMESPACE
%{rlibdir}/Runiversal/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora