%global packname  evir
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.7.1
Release:          1%{?dist}
Summary:          Extreme Values in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Functions for extreme value theory, which may be divided into the
following groups; exploratory data analysis, block maxima, peaks over
thresholds (univariate and bivariate), point processes, gev/gpd

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
%doc %{rlibdir}/evir/html
%doc %{rlibdir}/evir/DESCRIPTION
%{rlibdir}/evir/Meta
%{rlibdir}/evir/demo
%{rlibdir}/evir/CHANGES
%{rlibdir}/evir/help
%{rlibdir}/evir/NAMESPACE
%{rlibdir}/evir/INDEX
%{rlibdir}/evir/data
%{rlibdir}/evir/R
%{rlibdir}/evir/RCHANGES
%{rlibdir}/evir/README

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.1-1
- initial package for Fedora