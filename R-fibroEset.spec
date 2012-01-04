%global packname  fibroEset
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.6
Release:          1%{?dist}
Summary:          exprSet for Karaman et al. (2003) fibroblasts data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase 

%description
exprSet for Karaman et al. (2003) human, bonobo and gorilla fibroblasts

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
%doc %{rlibdir}/fibroEset/DESCRIPTION
%doc %{rlibdir}/fibroEset/html
%{rlibdir}/fibroEset/INDEX
%{rlibdir}/fibroEset/NAMESPACE
%{rlibdir}/fibroEset/data
%{rlibdir}/fibroEset/R
%{rlibdir}/fibroEset/Meta
%{rlibdir}/fibroEset/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.6-1
- initial package for Fedora