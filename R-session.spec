%global packname  session
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Functions for interacting with, saving and restoring R sessions.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Utility functions for interacting with R processes from external programs.
This package includes functions to save and restore session information
(including loaded packages, and attached data objects), as well as
functions to evaluate strings containing R commands and return the printed
results or an execution transcript.

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
%doc %{rlibdir}/session/html
%doc %{rlibdir}/session/NEWS
%doc %{rlibdir}/session/DESCRIPTION
%{rlibdir}/session/Meta
%{rlibdir}/session/help
%{rlibdir}/session/NAMESPACE
%{rlibdir}/session/ChangeLog
%{rlibdir}/session/INDEX
%{rlibdir}/session/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora