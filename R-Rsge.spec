%global packname  Rsge
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.3
Release:          1%{?dist}
Summary:          Interface to the SGE Queuing System

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-snow 

BuildRequires:    R-devel tex(latex) R-snow 

%description
This package provides functions for using R with the SGE cluster/grid
queuing system.

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
%doc %{rlibdir}/Rsge/html
%doc %{rlibdir}/Rsge/DESCRIPTION
%{rlibdir}/Rsge/Meta
%{rlibdir}/Rsge/CheckMemUsage.pl
%{rlibdir}/Rsge/INDEX
%{rlibdir}/Rsge/R
%{rlibdir}/Rsge/help
%{rlibdir}/Rsge/MonitorJob.sh
%{rlibdir}/Rsge/README
%{rlibdir}/Rsge/RunSgeJob

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.3-1
- initial package for Fedora