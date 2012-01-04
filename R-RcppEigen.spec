%global packname  RcppEigen
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Rcpp integration for the Eigen templated linear algebra library.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp R-Matrix 
Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Rcpp R-Matrix
BuildRequires:    R-Matrix 


%description
R and Eigen integration using Rcpp. . Eigen is a C++ template library for
linear algebra: matrices, vectors, numerical solvers and related
algorithms.  It supports dense and sparse matrices on integer, floating
point and complex numbers, decompositions of such matrices, and solutions
of linear systems. Its performance on many algorithms is comparable with
some of the best implementations based on Lapack and level-3 BLAS. . The
RcppEigen package includes the header files from the Eigen C++ template
library (currently version 3.0.3). Thus users do not need to install Eigen
itself in order to use RcppEigen. . Eigen is licensed under the GNU LGPL
version 3 or later, and also under the GNU GPL version 2 or later. 
RcppEigen (the Rcpp bindings/bridge to Eigen) is licensed under the GNU
GPL version 2 or later, as is the rest of Rcpp.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora