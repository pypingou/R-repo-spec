%global packname  affydata
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.11.15
Release:          1%{?dist}
Summary:          Affymetrix Data for Demonstration Purpose

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy 
Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-affy
BuildRequires:    R-methods 


%description
Example datasets of a slightly large size. They represent 'real world
examples', unlike the artificial examples included in the package affy.

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.11.15-1
- initial package for Fedora