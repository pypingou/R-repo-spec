%global packname  NPsimex
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Nonparametric Smoothing for contaminated data using Simulation-Extrapolation

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains a collection of functions to to perform
nonparametric deconvolution using simulation extrapolation (SIMEX). We
propose an estimator that adopts the SIMEX idea but bypasses the
simulation step in the original SIMEX algorithm. There is no bandwidth
parameter and the estimate is determined by appropriately selecting
"design points". See details in: Wang, X.F., Sun, J. and Fan, Z. (2011).
Deconvolution density estimation with heteroscedastic errors using SIMEX.

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
%doc %{rlibdir}/NPsimex/DESCRIPTION
%doc %{rlibdir}/NPsimex/html
%doc %{rlibdir}/NPsimex/NEWS
%{rlibdir}/NPsimex/script
%{rlibdir}/NPsimex/libs
%{rlibdir}/NPsimex/help
%{rlibdir}/NPsimex/Meta
%{rlibdir}/NPsimex/INDEX
%{rlibdir}/NPsimex/R
%{rlibdir}/NPsimex/LICENSE
%{rlibdir}/NPsimex/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora