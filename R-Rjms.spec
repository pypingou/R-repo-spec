%global packname  Rjms
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          R messaging using ActiveMQ and jms

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava R-Rjmsjars 

BuildRequires:    R-devel tex(latex) R-rJava R-Rjmsjars 

%description
This package uses rJava to publish messages to an activeMQ queue or topic,
implementing enterprise integration patterns.

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
%doc %{rlibdir}/Rjms/DESCRIPTION
%doc %{rlibdir}/Rjms/html
%{rlibdir}/Rjms/help
%{rlibdir}/Rjms/Meta
%{rlibdir}/Rjms/java
%{rlibdir}/Rjms/R
%{rlibdir}/Rjms/NAMESPACE
%{rlibdir}/Rjms/LICENSE
%{rlibdir}/Rjms/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.2-1
- initial package for Fedora