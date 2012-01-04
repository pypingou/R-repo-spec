%global packname  ElectroGraph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Enhanced routines for plotting and analyzing valued relational data.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains routines and procedures for relational data, namely
considerations for valued ties. In particular, relative distances may also
be calculated using Ohmic social conductance methods.

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
%doc %{rlibdir}/ElectroGraph/html
%doc %{rlibdir}/ElectroGraph/DESCRIPTION
%{rlibdir}/ElectroGraph/NAMESPACE
%{rlibdir}/ElectroGraph/help
%{rlibdir}/ElectroGraph/libs
%{rlibdir}/ElectroGraph/Meta
%{rlibdir}/ElectroGraph/INDEX
%{rlibdir}/ElectroGraph/demo
%{rlibdir}/ElectroGraph/data
%{rlibdir}/ElectroGraph/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.0-1
- initial package for Fedora