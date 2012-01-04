%global packname  PermAlgo
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Permutational algorithm to simulate survival data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This version of the permutational algorithm generates a dataset in which
event and censoring times are conditional on an user-specified list of
covariates, some or all of which are time-dependent.

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
%doc %{rlibdir}/PermAlgo/html
%doc %{rlibdir}/PermAlgo/DESCRIPTION
%doc %{rlibdir}/PermAlgo/CITATION
%{rlibdir}/PermAlgo/Meta
%{rlibdir}/PermAlgo/INDEX
%{rlibdir}/PermAlgo/R
%{rlibdir}/PermAlgo/NAMESPACE
%{rlibdir}/PermAlgo/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora