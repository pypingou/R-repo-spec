%global packname  paltran
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          WA, WA-PLS, MW for paleolimnology

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-vegan R-MASS R-mgcv 


BuildRequires:    R-devel tex(latex) R-vegan R-MASS R-mgcv



%description
This package contains functions for paleolimnology - wa-regression (see
also package analogue by G. Simpson!), wa-pls and the mowing-window
approch. The function palplot allows a first plot of the data including a
trend analysis. The mtf function is just a first test version.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.0-1
- initial package for Fedora