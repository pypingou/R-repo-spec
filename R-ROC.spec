%global packname  ROC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.0
Release:          1%{?dist}
Summary:          utilities for ROC, with uarray focus

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils R-methods 

BuildRequires:    R-devel tex(latex) R-utils R-methods 

%description
utilities for ROC, with uarray focus

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
%doc %{rlibdir}/ROC/DESCRIPTION
%doc %{rlibdir}/ROC/doc
%doc %{rlibdir}/ROC/html
%{rlibdir}/ROC/R
%{rlibdir}/ROC/NAMESPACE
%{rlibdir}/ROC/INDEX
%{rlibdir}/ROC/Meta
%{rlibdir}/ROC/libs
%{rlibdir}/ROC/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.0-1
- initial package for Fedora