%global packname  MVR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.00.0
Release:          1%{?dist}
Summary:          Mean-Variance Regularization

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-statmod R-snow 

BuildRequires:    R-devel tex(latex) R-statmod R-snow 

%description
MVR is a non-parametric method for joint adaptive mean-variance
regularization and variance stabilization of high-dimensional data. It is
suited for handling difficult problems posed by high-dimensional
multivariate datasets (p >> n paradigm), such as in omics-type data, among
which are that the variance is often a function of the mean,
variable-specific estimators of variances are not reliable, and tests
statistics have low powers due to a lack of degrees of freedom. Key
features include (i) Normalization and/or variance stabilization of the
data, (ii) Computation of mean-variance-regularized t- and F-statistics,
(iii) Generation of diverse diagnostic plots, (iv) Computationally
efficiency implementation, using C++ interfacing, and an option for
parallel computing to enjoy a fast and easy experience in the R

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.00.0-1
- initial package for Fedora