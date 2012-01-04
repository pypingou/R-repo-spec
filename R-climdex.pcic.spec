%global packname  climdex.pcic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          PCIC implementation of Climdex routines

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-PCICt R-caTools R-methods 


BuildRequires:    R-devel tex(latex) R-PCICt R-caTools R-methods



%description
The pcic_climdex package provides PCIC's implementation of Climdex
routines for computation of climate indices.

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
%doc %{rlibdir}/climdex.pcic/DESCRIPTION
%doc %{rlibdir}/climdex.pcic/html
/usr/lib/debug/.build-id/fe/55c51a9289338e825b2964a6c634020c7f3b3a
%{rlibdir}/climdex.pcic/Meta
%{rlibdir}/climdex.pcic/libs
%{rlibdir}/climdex.pcic/NAMESPACE
/usr/src/debug/climdex.pcic/climdex.pcic/src/zhang_running_quantile.cc
%{rlibdir}/climdex.pcic/R
%{rlibdir}/climdex.pcic/data
%{rlibdir}/climdex.pcic/help
%{rlibdir}/climdex.pcic/INDEX
/usr/lib/debug/.build-id/fe/55c51a9289338e825b2964a6c634020c7f3b3a.debug

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.1-1
- initial package for Fedora