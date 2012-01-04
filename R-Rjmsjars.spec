%global packname  Rjmsjars
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Rjms jars

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
External jars required for package Rjms.

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
%doc %{rlibdir}/Rjmsjars/html
%doc %{rlibdir}/Rjmsjars/DESCRIPTION
%{rlibdir}/Rjmsjars/LICENSE
%{rlibdir}/Rjmsjars/NAMESPACE
%{rlibdir}/Rjmsjars/help
%{rlibdir}/Rjmsjars/java
%{rlibdir}/Rjmsjars/Meta
%{rlibdir}/Rjmsjars/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora