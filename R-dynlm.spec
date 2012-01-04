%global packname  dynlm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Dynamic Linear Regression

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-zoo R-lmtest R-car 
Requires:         R-stats R-strucchange 

BuildRequires:    R-devel tex(latex) R-stats R-zoo R-lmtest R-car
BuildRequires:    R-stats R-strucchange 


%description
Dynamic linear models and time series regression.

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
%doc %{rlibdir}/dynlm/CITATION
%doc %{rlibdir}/dynlm/NEWS
%doc %{rlibdir}/dynlm/html
%doc %{rlibdir}/dynlm/DESCRIPTION
%{rlibdir}/dynlm/help
%{rlibdir}/dynlm/data
%{rlibdir}/dynlm/NAMESPACE
%{rlibdir}/dynlm/Meta
%{rlibdir}/dynlm/INDEX
%{rlibdir}/dynlm/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora