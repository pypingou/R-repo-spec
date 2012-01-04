%global packname  Rcpp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.7
Release:          1%{?dist}
Summary:          Seamless R and C++ Integration

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
The Rcpp package provides a C++ library which facilitates the integration
of R and C++. . R data types (SEXP) are matched to C++ objects in a class
hierarchy. All R types are supported (vectors, functions, environment, etc
...)  and each type is mapped to a dedicated class. For example, numeric
vectors are represented as instances of the Rcpp::NumericVector class,
environments are represented as instances of Rcpp::Environment, functions
are represented as Rcpp::Function, etc ... The "Rcpp-introduction"
vignette provides a good entry point to Rcpp. . Conversion from C++ to R
and back is driven by the templates Rcpp::wrap and Rcpp::as which are
highly flexible and extensible, as documented in the "Rcpp-extending"
vignette. . Rcpp also provides Rcpp modules, a framework that allows
exposing C++ functions and classes to the R level. The "Rcpp-modules"
vignette details the current set of features of Rcpp-modules. . Rcpp
includes a concept called Rcpp sugar that brings many R functions into
C++. Sugar takes advantage of lazy evaluation and expression templates to
achieve great performance while exposing a syntax that is much nicer to
use than the equivalent low-level loop code. The "Rcpp-sugar" vignette
gives an overview of the feature. . Several examples are included, and 753
unit tests in 338 unit test functions provide additional usage examples. .
An earlier version of Rcpp, containing what we now call the 'classic Rcpp
API' was written during 2005 and 2006 by Dominick Samperi. This code has
been factored out of Rcpp into the package RcppClassic and it is still
available for code relying on this interface. New development should use
this package instead.

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
%doc %{rlibdir}/Rcpp/DESCRIPTION
%doc %{rlibdir}/Rcpp/doc
%doc %{rlibdir}/Rcpp/html
%doc %{rlibdir}/Rcpp/CITATION
%doc %{rlibdir}/Rcpp/NEWS
%{rlibdir}/Rcpp/libs
%{rlibdir}/Rcpp/include
%{rlibdir}/Rcpp/unitTests
%{rlibdir}/Rcpp/INDEX
%{rlibdir}/Rcpp/R
%{rlibdir}/Rcpp/prompt
%{rlibdir}/Rcpp/help
%{rlibdir}/Rcpp/examples
%{rlibdir}/Rcpp/README
%{rlibdir}/Rcpp/announce
%{rlibdir}/Rcpp/NAMESPACE
%{rlibdir}/Rcpp/discovery
%{rlibdir}/Rcpp/Meta
%{rlibdir}/Rcpp/THANKS
%{rlibdir}/Rcpp/skeleton
%{rlibdir}/Rcpp/lib

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.7-1
- initial package for Fedora