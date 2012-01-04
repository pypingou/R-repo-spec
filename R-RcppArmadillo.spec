%global packname  RcppArmadillo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.33
Release:          1%{?dist}
Summary:          Rcpp integration for Armadillo templated linear algebra library

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp 


BuildRequires:    R-devel tex(latex) R-Rcpp



%description
R and Armadillo integration using Rcpp Armadillo is a templated C++ linear
algebra library (by Conrad Sanderson) that aims towards a good balance
between speed and ease of use. Integer, floating point and complex numbers
are supported, as well as a subset of trigonometric and statistics
functions. Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries. . A delayed evaluation
approach is employed (during compile time) to combine several operations
into one, and to reduce (or eliminate) the need for temporaries. This is
accomplished through recursive templates and template meta-programming. .
This library is useful if C++ has been decided as the language of choice
(due to speed and/or integration capabilities), rather than another
language. . The RcppArmadillo package includes the header files from the
templated Armadillo library (currently version 2.4.1). Thus users do not
need to install Armadillo itself in order to use RcppArmadillo. . This
Armadillo integration provides a nice illustration of the capabilities of
the Rcpp package for seamless R and C++ integration. . Armadillo is
licensed under the GNU LGPL version 3 or later, while RcppArmadillo (the
Rcpp bindings/bridge to Armadillo) is licenses under the GNU GPL version 2
or later, as is the rest of Rcpp.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.33-1
- initial package for Fedora