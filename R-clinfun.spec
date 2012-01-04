%global packname  clinfun
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.8
Release:          1%{?dist}
Summary:          Clinical Trial Design and Data Analysis Functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats 
Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-graphics R-stats
BuildRequires:    R-mvtnorm 


%description
Utilities to make your clinical collaborations easier if not fun.

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
%doc %{rlibdir}/clinfun/html
%doc %{rlibdir}/clinfun/DESCRIPTION
%{rlibdir}/clinfun/NAMESPACE
%{rlibdir}/clinfun/Meta
%{rlibdir}/clinfun/R
%{rlibdir}/clinfun/libs
%{rlibdir}/clinfun/INDEX
%{rlibdir}/clinfun/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.8-1
- initial package for Fedora