%global packname  ddst
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.02
Release:          1%{?dist}
Summary:          Data driven smooth test

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-orthopolynom R-evd 

BuildRequires:    R-devel tex(latex) R-orthopolynom R-evd 

%description
Support for data driven testing

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
%doc %{rlibdir}/ddst/html
%doc %{rlibdir}/ddst/DESCRIPTION
%{rlibdir}/ddst/INDEX
%{rlibdir}/ddst/help
%{rlibdir}/ddst/NAMESPACE
%{rlibdir}/ddst/Meta
%{rlibdir}/ddst/R
%{rlibdir}/ddst/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.02-1
- initial package for Fedora