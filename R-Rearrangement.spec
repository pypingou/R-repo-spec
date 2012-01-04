%global packname  Rearrangement
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Monotonize point and interval functional estimates by rearrangement

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-quantreg R-splines 


BuildRequires:    R-devel tex(latex) R-quantreg R-splines



%description
This package implements the rearrangement operator (Hardy, Littlewood, and
Polya 1952) for univariate, bivariate, and trivariate point estimates of
monotonic functions. It additionally provides a function that creates
simultaneous confidence intervals for univariate functions and applies the
rearrangement operator to these confidence intervals.

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
%doc %{rlibdir}/Rearrangement/doc
%doc %{rlibdir}/Rearrangement/DESCRIPTION
%doc %{rlibdir}/Rearrangement/html
%{rlibdir}/Rearrangement/INDEX
%{rlibdir}/Rearrangement/help
%{rlibdir}/Rearrangement/data
%{rlibdir}/Rearrangement/NAMESPACE
%{rlibdir}/Rearrangement/R
%{rlibdir}/Rearrangement/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora