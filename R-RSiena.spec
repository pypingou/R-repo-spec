%global packname  RSiena
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.12.167
Release:          1%{?dist}
Summary:          Siena - Simulation Investigation for Empirical Network Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Fits models to longitudinal networks

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
%doc %{rlibdir}/RSiena/html
%doc %{rlibdir}/RSiena/DESCRIPTION
%doc %{rlibdir}/RSiena/doc
%{rlibdir}/RSiena/examples
%{rlibdir}/RSiena/NAMESPACE
%{rlibdir}/RSiena/INDEX
%{rlibdir}/RSiena/Meta
%{rlibdir}/RSiena/ilcampo.gif
%{rlibdir}/RSiena/sienascript
%{rlibdir}/RSiena/R
%{rlibdir}/RSiena/help
%{rlibdir}/RSiena/libs
RPM build errors:
%{rlibdir}/RSiena/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.12.167-1
- initial package for Fedora