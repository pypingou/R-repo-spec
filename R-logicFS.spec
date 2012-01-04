%global packname  logicFS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Identification of SNP Interactions

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-LogicReg 

BuildRequires:    R-devel tex(latex) R-LogicReg 

%description
Identification of interactions between binary variables using Logic
Regression. Can, e.g., be used to find interesting SNP interactions.
Contains also a bagging version of logic regression for classification.

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
%doc %{rlibdir}/logicFS/html
%doc %{rlibdir}/logicFS/doc
%doc %{rlibdir}/logicFS/DESCRIPTION
%{rlibdir}/logicFS/help
%{rlibdir}/logicFS/data
%{rlibdir}/logicFS/Meta
%{rlibdir}/logicFS/INDEX
%{rlibdir}/logicFS/R
RPM build errors:
%{rlibdir}/logicFS/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora