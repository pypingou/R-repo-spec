%global packname  tsModel
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Time Series Modeling for Air Pollution and Health

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-splines R-stats R-tlnise R-MASS 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-splines R-stats R-tlnise R-MASS 


%description
Tools for specifying time series regression models

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
%doc %{rlibdir}/tsModel/DESCRIPTION
%doc %{rlibdir}/tsModel/COPYING
%doc %{rlibdir}/tsModel/html
%{rlibdir}/tsModel/R
%{rlibdir}/tsModel/NAMESPACE
%{rlibdir}/tsModel/data
%{rlibdir}/tsModel/INDEX
%{rlibdir}/tsModel/Meta
%{rlibdir}/tsModel/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.3-1
- initial package for Fedora