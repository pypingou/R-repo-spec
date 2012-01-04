%global packname  DSpat
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Spatial modelling for distance sampling data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-spatstat R-RandomFields R-gpclib R-mgcv 

BuildRequires:    R-devel tex(latex) R-spatstat R-RandomFields R-gpclib R-mgcv 

%description
Provides functions for fitting spatial models to line transect sampling
data and to estimate abundance within a region.

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
%doc %{rlibdir}/DSpat/html
%doc %{rlibdir}/DSpat/DESCRIPTION
%{rlibdir}/DSpat/data
%{rlibdir}/DSpat/help
%{rlibdir}/DSpat/Meta
%{rlibdir}/DSpat/INDEX
%{rlibdir}/DSpat/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora