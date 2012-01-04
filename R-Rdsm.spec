%global packname  Rdsm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Threads Environment for R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Provides a threads-type programming environment for R, usable both on a
multicore machine and across a network of multiple machines.  The package
gives the programmer a shared memory world view, again even across
multiple machines on a network.

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
%doc %{rlibdir}/Rdsm/DESCRIPTION
%doc %{rlibdir}/Rdsm/html
%{rlibdir}/Rdsm/testscripts
%{rlibdir}/Rdsm/README
%{rlibdir}/Rdsm/AutoLaunch.R
%{rlibdir}/Rdsm/help
%{rlibdir}/Rdsm/INDEX
%{rlibdir}/Rdsm/examples
%{rlibdir}/Rdsm/Meta
%{rlibdir}/Rdsm/R
%{rlibdir}/Rdsm/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora