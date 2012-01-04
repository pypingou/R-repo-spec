%global packname  RcmdrPlugin.UCA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          UCA Rcmdr Plug-in

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr 


BuildRequires:    R-devel tex(latex) R-Rcmdr



%description
This package provides customized function for R-Commander made by R-UCA

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
%doc %{rlibdir}/RcmdrPlugin.UCA/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.UCA/html
%{rlibdir}/RcmdrPlugin.UCA/NAMESPACE
%{rlibdir}/RcmdrPlugin.UCA/help
%{rlibdir}/RcmdrPlugin.UCA/po
%{rlibdir}/RcmdrPlugin.UCA/R
%{rlibdir}/RcmdrPlugin.UCA/etc
%{rlibdir}/RcmdrPlugin.UCA/INDEX
%{rlibdir}/RcmdrPlugin.UCA/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora