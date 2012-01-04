%global packname  varSelRF
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.3
Release:          1%{?dist}
Summary:          Variable selection using random forests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-randomForest 

BuildRequires:    R-devel tex(latex) R-randomForest 

%description
Variable selection from random forests using both backwards variable
elimination (for the selection of small sets of non-redundant variables)
and selection based on the importance spectrum (somewhat similar to scree
plots; for the selection of large, potentially highly-correlated
variables). Main applications in high-dimensional data (e.g., microarray
data, and other genomics and proteomics applications). You can use rpvm
instead of Rmpi if you want but I've only tested with Rmpi.

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
%doc %{rlibdir}/varSelRF/html
%doc %{rlibdir}/varSelRF/DESCRIPTION
%{rlibdir}/varSelRF/INDEX
%{rlibdir}/varSelRF/Meta
%{rlibdir}/varSelRF/R
%{rlibdir}/varSelRF/NAMESPACE
%{rlibdir}/varSelRF/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.3-1
- initial package for Fedora