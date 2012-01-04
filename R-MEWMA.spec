%global packname  MEWMA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Multivariate Exponentially Weighted Moving Average (MEWMA) Control Chart

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
mewma package perform the Multivariate Exponentially Weighted Moving
Average (MEWMA) Control Chart

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
%doc %{rlibdir}/MEWMA/DESCRIPTION
%doc %{rlibdir}/MEWMA/html
%{rlibdir}/MEWMA/Meta
%{rlibdir}/MEWMA/NAMESPACE
%{rlibdir}/MEWMA/help
%{rlibdir}/MEWMA/INDEX
%{rlibdir}/MEWMA/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora