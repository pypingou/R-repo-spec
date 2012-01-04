%global packname  RQuantLib
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.8
Release:          1%{?dist}
Summary:          R interface to the QuantLib library

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp 


BuildRequires:    R-devel tex(latex) R-Rcpp



%description
The RQuantLib package makes parts of QuantLib visible to the R user.
Currently a number option pricing functions are included, both vanilla and
exotic, as well as a broad range of fixed-income functions. Also included
are general calendaring and holiday utilities. Further software
contributions are welcome. . The QuantLib project aims to provide a
comprehensive software framework for quantitative finance. The goal is to
provide a standard open source library for quantitative analysis,
modeling, trading, and risk management of financial assets. . The Windows
binary version is self-contained and does not require a QuantLib (or
Boost) installation. . RQuantLib uses the Rcpp R/C++ interface class
library. See the Rcpp package on CRAN (or R-Forge) for more information on
Rcpp. . Note that while RQuantLib's code is licensed under the GPL (v2 or
later), QuantLib itself is released under a somewhat less restrictive Open
Source license (see QuantLib-License.txt).

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.8-1
- initial package for Fedora