%global packname  RcmdrPlugin.coin
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.20
Release:          1%{?dist}
Summary:          Rcmdr Coin Plug-In

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-20.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-coin R-survival R-multcomp 


BuildRequires:    R-devel tex(latex) R-Rcmdr R-coin R-survival R-multcomp



%description
This package provides an Rcmdr "plug-in" based on coin (Conditional
Inference Procedures in a Permutation Test Framework).

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
%doc %{rlibdir}/RcmdrPlugin.coin/html
%doc %{rlibdir}/RcmdrPlugin.coin/DESCRIPTION
%{rlibdir}/RcmdrPlugin.coin/Meta
%{rlibdir}/RcmdrPlugin.coin/NAMESPACE
%{rlibdir}/RcmdrPlugin.coin/R
%{rlibdir}/RcmdrPlugin.coin/etc
%{rlibdir}/RcmdrPlugin.coin/help
%{rlibdir}/RcmdrPlugin.coin/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.20-1
- initial package for Fedora