%global packname  sandwich
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.8
Release:          1%{?dist}
Summary:          Robust Covariance Matrix Estimators

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-zoo 

BuildRequires:    R-devel tex(latex) R-stats R-zoo 

%description
Model-robust standard error estimators for cross-sectional, time series
and longitudinal data.

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
%doc %{rlibdir}/sandwich/doc
%doc %{rlibdir}/sandwich/DESCRIPTION
%doc %{rlibdir}/sandwich/CITATION
%doc %{rlibdir}/sandwich/NEWS
%doc %{rlibdir}/sandwich/html
%{rlibdir}/sandwich/INDEX
%{rlibdir}/sandwich/data
%{rlibdir}/sandwich/NAMESPACE
%{rlibdir}/sandwich/help
%{rlibdir}/sandwich/R
%{rlibdir}/sandwich/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.8-1
- initial package for Fedora