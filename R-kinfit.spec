%global packname  kinfit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.06
Release:          1%{?dist}
Summary:          Routines for fitting kinetic models to chemical degradation data

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Simple calculation routines based on the FOCUS Kinetics Report (2006).
Only kinetic models for parent only datasets are included (no metabolite
formation/decline or multicompartment kinetics). Please note that no
warranty is implied for correctness of results or fitness for a particular

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
%doc %{rlibdir}/kinfit/DESCRIPTION
%doc %{rlibdir}/kinfit/doc
%doc %{rlibdir}/kinfit/html
%{rlibdir}/kinfit/Meta
%{rlibdir}/kinfit/NAMESPACE
RPM build errors:
%{rlibdir}/kinfit/data
%{rlibdir}/kinfit/help
%{rlibdir}/kinfit/R
%{rlibdir}/kinfit/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.06-1
- initial package for Fedora