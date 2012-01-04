%global packname  distrEllipse
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          S4 classes for elliptically contoured distributions

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-graphics R-mvtnorm R-setRNG R-distr R-distrEx R-distrSim R-startupmsg 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-mvtnorm R-setRNG R-distr R-distrEx R-distrSim R-startupmsg 

%description
Distribution (S4-)classes for elliptically contoured distributions (based
on package distr)

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
%doc %{rlibdir}/distrEllipse/NEWS
%doc %{rlibdir}/distrEllipse/html
%doc %{rlibdir}/distrEllipse/DESCRIPTION
%doc %{rlibdir}/distrEllipse/CITATION
%{rlibdir}/distrEllipse/TOBEDONE
%{rlibdir}/distrEllipse/Meta
%{rlibdir}/distrEllipse/INDEX
%{rlibdir}/distrEllipse/help
%{rlibdir}/distrEllipse/R
%{rlibdir}/distrEllipse/NAMESPACE
%{rlibdir}/distrEllipse/MASKING

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.1-1
- initial package for Fedora