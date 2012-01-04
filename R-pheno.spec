%global packname  pheno
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Auxiliary functions for phenological data analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nlme R-SparseM R-quantreg 


BuildRequires:    R-devel tex(latex) R-nlme R-SparseM R-quantreg



%description
Provides some easy-to-use functions for time series analyses of (plant-)
phenological data sets. These functions mainly deal with the estimation of
combined phenological time series and are usually wrappers for functions
that are already implemented in other R packages adapted to the special
structure of phenological data and the needs of phenologists. Some date
conversion functions to handle Julian dates are also provided.

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
%doc %{rlibdir}/pheno/DESCRIPTION
%doc %{rlibdir}/pheno/html
%{rlibdir}/pheno/libs
%{rlibdir}/pheno/Meta
%{rlibdir}/pheno/help
%{rlibdir}/pheno/INDEX
%{rlibdir}/pheno/data
%{rlibdir}/pheno/R
%{rlibdir}/pheno/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora