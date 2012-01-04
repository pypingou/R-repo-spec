%global packname  nws
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.7.0.1
Release:          1%{?dist}
Summary:          R functions for NetWorkSpaces and Sleigh

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Provides coordination and parallel execution facilities, as well as
limited cross-language data exchange, using the netWorkSpaces server
developed by REvolution Computing

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
%doc %{rlibdir}/nws/html
%doc %{rlibdir}/nws/DESCRIPTION
%{rlibdir}/nws/data
%{rlibdir}/nws/INDEX
%{rlibdir}/nws/bin
%{rlibdir}/nws/NAMESPACE
%{rlibdir}/nws/R
%{rlibdir}/nws/README
%{rlibdir}/nws/ChangeLog
%{rlibdir}/nws/README.sleigh
%{rlibdir}/nws/examples
%{rlibdir}/nws/help
%{rlibdir}/nws/demo
%{rlibdir}/nws/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.0.1-1
- initial package for Fedora