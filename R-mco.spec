%global packname  mco
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.9
Release:          1%{?dist}
Summary:          Multi criteria optimization algorithms and related functions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions for multi criteria optimization using genetic algorithms and
related test problems

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
%doc %{rlibdir}/mco/html
%doc %{rlibdir}/mco/DESCRIPTION
%{rlibdir}/mco/help
%{rlibdir}/mco/INDEX
%{rlibdir}/mco/Meta
%{rlibdir}/mco/R
%{rlibdir}/mco/libs
RPM build errors:
%{rlibdir}/mco/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.9-1
- initial package for Fedora