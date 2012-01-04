%global packname  texmex
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Threshold exceedences and multivariate extremes

Group:            Applications/Engineering 
License:          GPL (>= 2) | BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Conditional multivariate extreme value modelling using the approach of
Heffernan and Tawn.

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
%doc %{rlibdir}/texmex/html
%doc %{rlibdir}/texmex/DESCRIPTION
%{rlibdir}/texmex/data
%{rlibdir}/texmex/help
%{rlibdir}/texmex/R
%{rlibdir}/texmex/Meta
%{rlibdir}/texmex/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora