%global packname  ftnonpar
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.84
Release:          1%{?dist}
Summary:          Features and Strings for Nonparametric Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-84.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package contains R-functions to perform the methods in nonparametric
regression and density estimation, described in Davies, P. L. and Kovac,
A. (2001) Local Extremes, Runs, Strings and Multiresolution (with
discussion) Annals of Statistics. 29. p1-65 Davies, P. L. and Kovac, A.
(2004) Densities, Spectral Densities and Modality Annals of Statistics.
Annals of Statistics. 32. p1093-1136 Kovac, A. (2006) Smooth functions and
local extreme values. Computational Statistics and Data Analysis (to
appear) D\"umbgen, L. and Kovac, A. (2006) Extensions of smoothing via
taut strings Davies, P. L. (1995) Data features. Statistica Neerlandica

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
%doc %{rlibdir}/ftnonpar/html
%doc %{rlibdir}/ftnonpar/DESCRIPTION
%{rlibdir}/ftnonpar/NAMESPACE
%{rlibdir}/ftnonpar/Meta
%{rlibdir}/ftnonpar/R
%{rlibdir}/ftnonpar/INDEX
%{rlibdir}/ftnonpar/data
%{rlibdir}/ftnonpar/help
%{rlibdir}/ftnonpar/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.84-1
- initial package for Fedora