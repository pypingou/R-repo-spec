%global packname  monomvn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.6
Release:          1%{?dist}
Summary:          Estimation for multivariate normal and Student-t data with monotone missingness

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.8-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-pls R-lars R-MASS 

BuildRequires:    R-devel tex(latex) R-pls R-lars R-MASS 

%description
Estimation of multivariate normal and student-t data of arbitrary
dimension where the pattern of missing data is monotone. Through the use
of parsimonious/shrinkage regressions (plsr, pcr, lasso, ridge, etc.),
where standard regressions fail, the package can handle a nearly arbitrary
amount of missing data. The current version supports maximum likelihood
inference and a full Bayesian approach employing scale-mixtures for the
lasso (double-exponential) and Normal-Gamma priors, and Student-t errors. 
Monotone data augmentation extends this Bayesian approach to arbitrary
missingness patterns. A fully functional standalone interface to the
Bayesian lasso (from Park & Casella), Normal-Gamma (from Griffin & Brown),
and ridge regression with model selection via Reversible Jump, and
student-t errors (from Geweke) is also provided

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.6-1
- initial package for Fedora