%global packname  delt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.0
Release:          1%{?dist}
Summary:          Estimation of multivariate densities with adaptive histograms

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-denpro 

BuildRequires:    R-devel tex(latex) R-denpro 

%description
The package implements methods for estimating multivariate densities:
adaptive histograms (greedy histograms and CART-histograms), stagewise
minimization, and bootstrap aggregation are included in the package.

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
%doc %{rlibdir}/delt/html
%doc %{rlibdir}/delt/DESCRIPTION
%{rlibdir}/delt/libs
%{rlibdir}/delt/Meta
%{rlibdir}/delt/NAMESPACE
%{rlibdir}/delt/INDEX
%{rlibdir}/delt/R
%{rlibdir}/delt/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.0-1
- initial package for Fedora