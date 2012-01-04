%global packname  termstrc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.4
Release:          1%{?dist}
Summary:          Zero-coupon Yield Curve Estimation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp R-zoo R-rgl R-lmtest 
Requires:         R-urca R-sandwich 

BuildRequires:    R-devel tex(latex) R-Rcpp R-zoo R-rgl R-lmtest
BuildRequires:    R-urca R-sandwich 


%description
The package offers a wide range of functions for term structure estimation
based on static and dynamic coupon bond and yield data sets. The
implementation focuses on the cubic splines approach of McCulloch (1971,
1975) and the Nelson and Siegel (1987) method with extensions by Svensson
(1994), Diebold and Li (2006) and De Pooter (2007). We propose a weighted
constrained optimization procedure with analytical gradients and a
globally optimal start parameter search algorithm. Extensive summary
statistics and plots are provided to compare the results of the different
estimation methods. Several demos are available using data from European
government bonds and yields.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.4-1
- initial package for Fedora