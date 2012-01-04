%global packname  robeth
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          R functions for robust statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Locations problems, M-estimates of coefficients and scale in linear
regression, Weights for bounded influence regression, Covariance matrix of
the coefficient estimates, Asymptotic relative efficiency of regression
M-estimates, Robust testing in linear models, High breakdown point
regression, M-estimates of covariance matrices, M-estimates for discrete
generalized linear models.

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
%doc %{rlibdir}/robeth/html
%doc %{rlibdir}/robeth/DESCRIPTION
RPM build errors:
%{rlibdir}/robeth/INDEX
%{rlibdir}/robeth/help
%{rlibdir}/robeth/Meta
%{rlibdir}/robeth/libs
%{rlibdir}/robeth/NAMESPACE
%{rlibdir}/robeth/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora