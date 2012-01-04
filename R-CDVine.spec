%global packname  CDVine
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Statistical inference of C- and D-vine copulas

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-mvtnorm R-igraph 

BuildRequires:    R-devel tex(latex) R-MASS R-mvtnorm R-igraph 

%description
This package provides functions for statistical inference of canonical
vine (C-vine) and D-vine copulas. It contains tools for bivariate
exploratory data analysis and for bivariate as well as vine copula
selection. Models can be estimated either sequentially or by joint maximum
likelihood estimation. Sampling algorithms and plotting methods are also
included. Data is assumed to lie in the unit hypercube (so-called copula

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.4-1
- initial package for Fedora