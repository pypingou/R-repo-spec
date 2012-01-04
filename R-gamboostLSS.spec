%global packname  gamboostLSS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Boosting Methods for GAMLSS Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splines R-survival R-methods R-mboost 

BuildRequires:    R-devel tex(latex) R-splines R-survival R-methods R-mboost 

%description
Boosting models for fitting generalized additive models for location,
shape and scale (gamLSS models) to potentially high dimensional data.

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
%doc %{rlibdir}/gamboostLSS/html
%doc %{rlibdir}/gamboostLSS/NEWS
%doc %{rlibdir}/gamboostLSS/CITATION
%doc %{rlibdir}/gamboostLSS/DESCRIPTION
%{rlibdir}/gamboostLSS/R
%{rlibdir}/gamboostLSS/INDEX
%{rlibdir}/gamboostLSS/help
%{rlibdir}/gamboostLSS/NAMESPACE
%{rlibdir}/gamboostLSS/Meta
%{rlibdir}/gamboostLSS/CHANGES

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora