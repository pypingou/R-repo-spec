%global packname  RandomFields
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.53
Release:          1%{?dist}
Summary:          Simulation and Analysis of Random Fields

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Simulation of Gaussian and extreme value random fields; conditional
simulation; kriging

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
%doc %{rlibdir}/RandomFields/html
%doc %{rlibdir}/RandomFields/DESCRIPTION
%{rlibdir}/RandomFields/Meta
%{rlibdir}/RandomFields/data
RPM build errors:
%{rlibdir}/RandomFields/R
%{rlibdir}/RandomFields/NAMESPACE
%{rlibdir}/RandomFields/help
%{rlibdir}/RandomFields/INDEX
%{rlibdir}/RandomFields/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.53-1
- initial package for Fedora