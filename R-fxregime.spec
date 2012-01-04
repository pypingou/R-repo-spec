%global packname  fxregime
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Exchange Rate Regime Analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-zoo R-sandwich R-strucchange 
Requires:         R-graphics R-stats R-zoo R-sandwich R-strucchange R-car 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-zoo R-sandwich R-strucchange
BuildRequires:    R-graphics R-stats R-zoo R-sandwich R-strucchange R-car 


%description
Exchange rate regression and structural change tools for estimating,
testing, dating, and monitoring (de facto) exchange rate regimes.

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
%doc %{rlibdir}/fxregime/doc
%doc %{rlibdir}/fxregime/CITATION
%doc %{rlibdir}/fxregime/DESCRIPTION
%doc %{rlibdir}/fxregime/NEWS
%doc %{rlibdir}/fxregime/html
%{rlibdir}/fxregime/INDEX
%{rlibdir}/fxregime/Meta
%{rlibdir}/fxregime/data
%{rlibdir}/fxregime/help
%{rlibdir}/fxregime/R
%{rlibdir}/fxregime/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora