%global packname  verification
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.31
Release:          1%{?dist}
Summary:          Forecast verification utilities.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-waveslim R-fields R-boot R-CircStats 


BuildRequires:    R-devel tex(latex) R-methods R-waveslim R-fields R-boot R-CircStats



%description
This package contains utilities for verification of discrete,continuous,
probabilistic forecasts and forecast expressed as parametric

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
%doc %{rlibdir}/verification/html
%doc %{rlibdir}/verification/DESCRIPTION
%doc %{rlibdir}/verification/doc
%{rlibdir}/verification/data
%{rlibdir}/verification/NAMESPACE
%{rlibdir}/verification/R
%{rlibdir}/verification/help
%{rlibdir}/verification/Meta
%{rlibdir}/verification/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.31-1
- initial package for Fedora