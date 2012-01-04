%global packname  factorQR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Bayesian quantile regression factor models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
Package to fit Bayesian quantile regression models that assume a factor
structure for at least part of the design matrix.

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
%doc %{rlibdir}/factorQR/DESCRIPTION
%doc %{rlibdir}/factorQR/html
%{rlibdir}/factorQR/help
%{rlibdir}/factorQR/Meta
%{rlibdir}/factorQR/libs
%{rlibdir}/factorQR/NAMESPACE
%{rlibdir}/factorQR/INDEX
%{rlibdir}/factorQR/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora