%global packname  snow
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.7
Release:          1%{?dist}
Summary:          Simple Network of Workstations

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Support for simple parallel computing in R.

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
%doc %{rlibdir}/snow/html
%doc %{rlibdir}/snow/DESCRIPTION
%{rlibdir}/snow/NAMESPACE
%{rlibdir}/snow/RPVMnode.sh
%{rlibdir}/snow/RNWSnode.sh
%{rlibdir}/snow/RMPInode.R
%{rlibdir}/snow/RSOCKnode.R
%{rlibdir}/snow/RMPInode.sh
%{rlibdir}/snow/RPVMnode.R
%{rlibdir}/snow/RSOCKnode.sh
%{rlibdir}/snow/INDEX
%{rlibdir}/snow/RMPISNOWprofile
%{rlibdir}/snow/help
%{rlibdir}/snow/Meta
%{rlibdir}/snow/RunSnowNode
%{rlibdir}/snow/RMPISNOW
%{rlibdir}/snow/RNWSnode.R
%{rlibdir}/snow/RunSnowWorker
%{rlibdir}/snow/RunSnowWorker.bat
%{rlibdir}/snow/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.7-1
- initial package for Fedora