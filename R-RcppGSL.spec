%global packname  RcppGSL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Rcpp integration for GNU GSL vectors and matrices

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp 


BuildRequires:    R-devel tex(latex) R-Rcpp



%description
Rcpp integration for GNU GSL vectors and matrices The GNU Scientific
Library (GSL) is a collection of numerical routines for scientifc
computing. It is particularly useful for C and C++ programs as it provides
a standard C interface to a wide range of mathematical routines such as
special functions, permutations, combinations, fast fourier transforms,
eigensystems, random numbers, quadrature, random distributions,
quasi-random sequences, Monte Carlo integration, N-tuples, differential
equations, simulated annealing, numerical differentiation, interpolation,
series acceleration, Chebyshev approximations, root-finding, discrete
Hankel transforms physical constants, basis splines and wavelets.  There
are over 1000 functions in total with an extensive test suite. . The
RcppGSL package provides an easy-to-use interface between GSL data
structures and R using concepts from Rcpp which is itself a package that
eases the interfaces between R and C++.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora