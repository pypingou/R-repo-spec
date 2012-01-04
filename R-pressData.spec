%global packname  pressData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Data sets for package PRESS--Protein REsidue-level Structural Statistics

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Data sets for displaying statistical information about known protein
structures and for evaluating the energy of novel structures.

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
%doc %{rlibdir}/pressData/DESCRIPTION
%doc %{rlibdir}/pressData/html
%{rlibdir}/pressData/help
%{rlibdir}/pressData/data
%{rlibdir}/pressData/NAMESPACE
%{rlibdir}/pressData/INDEX
%{rlibdir}/pressData/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora