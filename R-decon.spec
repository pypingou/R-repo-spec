%global packname  decon
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Deconvolution Estimation in Measurement Error Models

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains a collection of functions to deal with nonparametric
measurement error problems using deconvolution kernel methods. We focus
two measurement error models in the package: (1) an additive measurement
error model, where the goal is to estimate the density or distribution
function from contaminated data; (2) nonparametric regression model with
errors-in-variables. The R functions allow the measurement errors to be
either homoscedastic or heteroscedastic. To make the deconvolution
estimators computationally more efficient in R, we adapt the "Fast Fourier
Transform" (FFT) algorithm for density estimation with error-free data to
the deconvolution kernel estimation. Several methods for the selection of
the data-driven smoothing parameter are also provided in the package. See
details in: Wang, X.F. and Wang, B. (2011). Deconvolution estimation in
measurement error models: The R package decon. Journal of Statistical
Software, 39(10), 1-24.

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
%doc %{rlibdir}/decon/NEWS
%doc %{rlibdir}/decon/html
%doc %{rlibdir}/decon/CITATION
%doc %{rlibdir}/decon/DESCRIPTION
%{rlibdir}/decon/LICENSE
%{rlibdir}/decon/Meta
%{rlibdir}/decon/script
%{rlibdir}/decon/libs
%{rlibdir}/decon/NAMESPACE
%{rlibdir}/decon/help
%{rlibdir}/decon/data
%{rlibdir}/decon/INDEX
%{rlibdir}/decon/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora