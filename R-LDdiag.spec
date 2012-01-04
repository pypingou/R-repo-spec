%global packname  LDdiag
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Link Function and Distribution Diagnostic Test for Social Science Researchers

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
Social science researchers sometimes have difficulties in deciding
appropriate regression methods and/or link functions for their studies.
This package provides some model diagonistic approaches for link function
and distribution, such as Pregibon linearity test, Hosmer-Lemeshow test,
Copas test, Park test, etc.

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
%doc %{rlibdir}/LDdiag/DESCRIPTION
%doc %{rlibdir}/LDdiag/html
%{rlibdir}/LDdiag/R
%{rlibdir}/LDdiag/Meta
%{rlibdir}/LDdiag/INDEX
%{rlibdir}/LDdiag/NAMESPACE
%{rlibdir}/LDdiag/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora