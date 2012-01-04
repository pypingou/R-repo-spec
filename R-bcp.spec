%global packname  bcp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.0.0
Release:          1%{?dist}
Summary:          A Package for Performing a Bayesian Analysis of Change Point Problems

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats R-graphics R-foreach R-grid R-Rcpp 


BuildRequires:    R-devel tex(latex) R-methods R-stats R-graphics R-foreach R-grid R-Rcpp



%description
This package provides an implementation of an approximation to the Barry
and Hartigan (1993) product partition model for the normal errors change
point problem using Markov Chain Monte Carlo.  It also extends the
methodology to independent multivariate series with an assumed common
change point structure.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0.0-1
- initial package for Fedora