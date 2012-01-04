%global packname  LTPDvar
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          LTPD plans for sampling inspection by variables

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Calculation and evaluation of LTPD plans for sampling inspection by

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
%doc %{rlibdir}/LTPDvar/DESCRIPTION
%doc %{rlibdir}/LTPDvar/html
%{rlibdir}/LTPDvar/R
%{rlibdir}/LTPDvar/NAMESPACE
%{rlibdir}/LTPDvar/help
%{rlibdir}/LTPDvar/INDEX
%{rlibdir}/LTPDvar/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora