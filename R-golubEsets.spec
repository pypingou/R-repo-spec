%global packname  golubEsets
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.9
Release:          1%{?dist}
Summary:          exprSets for golub leukemia data

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
representation of public golub data with some covariate data of provenance
unknown to the maintainer at present; now employs ExpressionSet format

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
%doc %{rlibdir}/golubEsets/html
%doc %{rlibdir}/golubEsets/DESCRIPTION
%{rlibdir}/golubEsets/data
%{rlibdir}/golubEsets/help
%{rlibdir}/golubEsets/NAMESPACE
%{rlibdir}/golubEsets/INDEX
%{rlibdir}/golubEsets/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.9-1
- initial package for Fedora