%global packname  Matching
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.7.14
Release:          1%{?dist}
Summary:          Multivariate and Propensity Score Matching with Balance Optimization

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.7-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rgenoud R-MASS R-graphics R-grDevices R-stats 

BuildRequires:    R-devel tex(latex) R-rgenoud R-MASS R-graphics R-grDevices R-stats 

%description
Provides functions for multivariate and propensity score matching and for
finding optimal balance based on a genetic search algorithm. A variety of
univariate and multivariate metrics to determine if balance has been
obtained are also provided.

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
%doc %{rlibdir}/Matching/CITATION
%doc %{rlibdir}/Matching/html
%doc %{rlibdir}/Matching/DESCRIPTION
%{rlibdir}/Matching/demo
%{rlibdir}/Matching/NAMESPACE
%{rlibdir}/Matching/help
%{rlibdir}/Matching/INDEX
%{rlibdir}/Matching/data
%{rlibdir}/Matching/libs
%{rlibdir}/Matching/R
%{rlibdir}/Matching/Meta
%{rlibdir}/Matching/extras

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.7.14-1
- initial package for Fedora