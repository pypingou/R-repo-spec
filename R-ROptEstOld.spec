%global packname  ROptEstOld
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Optimally robust estimation - old version

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-distr R-distrEx R-RandVar 

BuildRequires:    R-devel tex(latex) R-methods R-distr R-distrEx R-RandVar 

%description
Optimally robust estimation using S4 classes and methods. Old version
still needed for current versions of ROptRegTS and RobRex.

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
%doc %{rlibdir}/ROptEstOld/NEWS
%doc %{rlibdir}/ROptEstOld/html
%doc %{rlibdir}/ROptEstOld/DESCRIPTION
%{rlibdir}/ROptEstOld/NAMESPACE
%{rlibdir}/ROptEstOld/R
%{rlibdir}/ROptEstOld/Meta
%{rlibdir}/ROptEstOld/TOBEDONE
%{rlibdir}/ROptEstOld/INDEX
%{rlibdir}/ROptEstOld/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- initial package for Fedora